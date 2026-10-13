"""Native inventory discovery is allowed only inside the scoped paper profile."""
import copy,json,unittest
import codex_transport as t

class PaperDiscoveryTests(unittest.TestCase):
    def live(self,args=None):
        return {'type':'item.started','item':{'type':'mcp_tool_call','server':'codex','tool':'list_mcp_resources','arguments':{} if args is None else args}}
    def stored(self,args=None):
        args={} if args is None else args
        return {'rollout_event_type':'response_item','payload_type':'function_call','namespace':None,'name':'list_mcp_resources','arguments_canonical_sha256':t.sha256_text(json.dumps(args,ensure_ascii=False,separators=(',',':')))}
    def test_live_and_persisted_exact_inventory(self):
        for args in ({},{'server':'merlean_paper'}):
            for role in ('author','review'):
                self.assertTrue(t._allowed_paper_event(self.live(args),role))
                self.assertTrue(t._allowed_persisted_paper_event(self.stored(args),role))
        self.assertFalse(t._allowed_paper_event(self.live(),'main'))
        self.assertFalse(t._allowed_persisted_paper_event(self.stored(),'main'))
    def test_no_read_template_other_server_or_extra_argument(self):
        for args in ({'server':'other'},{'cursor':'x'},{'uri':'file:///secret'},{'server':'merlean_paper','uri':'x'},[],None):
            live=self.live();live['item']['arguments']=args
            self.assertFalse(t._allowed_paper_event(live,'author'))
            if args is not None:self.assertFalse(t._allowed_persisted_paper_event(self.stored(args),'author'))
        for name in ('read_mcp_resource','shell','spawn_agent'):
            live=self.live();live['item']['tool']=name;stored=self.stored();stored['name']=name
            self.assertFalse(t._allowed_paper_event(live,'author'))
            self.assertFalse(t._allowed_persisted_paper_event(stored,'author'))
        for key,value in (('namespace','functions'),('namespace','mcp__other'),('payload_type','custom_tool_call'),('arguments_canonical_sha256',None)):
            stored=self.stored();stored[key]=value;self.assertFalse(t._allowed_persisted_paper_event(stored,'author'))
        for key,value in (('server','other'),('type','command_execution')):
            live=self.live();live['item'][key]=value;self.assertFalse(t._allowed_paper_event(live,'author'))
    def test_rejected_recovery_category_is_strict_and_nonmutating(self):
        meta={'status':'invalid_tool_attempt','module':'paper-light-author','model_verified':True,'persisted_rollout_audit':{'status':'verified'},'protocol_errors':[],
              'tool_events':[{'event':self.live()}],'persisted_tool_events':[self.stored()]}
        before=copy.deepcopy(meta);self.assertTrue(t.only_benign_paper_discovery_violation(meta));self.assertEqual(meta,before)
        for key,value in (('status','completed'),('module','main'),('model_verified',False),('protocol_errors',['bad']),('failure_codes',['quota']),('tool_events',[]),('persisted_tool_events',[]),('persisted_rollout_audit',{'status':'unknown'})):
            bad=copy.deepcopy(meta);bad[key]=value;self.assertFalse(t.only_benign_paper_discovery_violation(bad))
        bad=copy.deepcopy(meta);bad['persisted_tool_events'].append({**self.stored(),'name':'read_mcp_resource'});self.assertFalse(t.only_benign_paper_discovery_violation(bad))
    def test_templates_prospective_only(self):
        for args in ({}, {'server':'merlean_paper'}):
            live=self.live(args);live['item']['tool']='list_mcp_resource_templates'
            stored=self.stored(args);stored['name']='list_mcp_resource_templates'
            for role in ('author','review'):
                self.assertTrue(t._allowed_paper_event(live,role))
                self.assertTrue(t._allowed_persisted_paper_event(stored,role))
            self.assertFalse(t._allowed_paper_event(live,'main'))
            self.assertFalse(t._allowed_persisted_paper_event(stored,'main'))
            self.assertFalse(t._allowed_paper_discovery_event(live,resources_only=True))
            self.assertFalse(t._allowed_persisted_paper_discovery(stored,resources_only=True))
            meta={'status':'invalid_tool_attempt','module':'paper-light-author','model_verified':True,'persisted_rollout_audit':{'status':'verified'},'tool_events':[{'event':live}],'persisted_tool_events':[stored]}
            self.assertFalse(t.only_benign_paper_discovery_violation(meta))
        for args in ({'server':'other'},{'cursor':'x'},{'server':'merlean_paper','uri':'x'}):
            live=self.live(args);live['item']['tool']='list_mcp_resource_templates'
            stored=self.stored(args);stored['name']='list_mcp_resource_templates'
            self.assertFalse(t._allowed_paper_event(live,'author'))
            self.assertFalse(t._allowed_persisted_paper_event(stored,'author'))

    def test_actual_named_server_templates_envelope(self):
        event=self.live({'server':'merlean_paper'})
        event['item'].update(server='merlean_paper',tool='list_mcp_resource_templates')
        self.assertTrue(t._allowed_paper_event(event,'author'))
        self.assertFalse(t._allowed_paper_discovery_event(event,resources_only=True))
        resource=copy.deepcopy(event);resource['item']['tool']='list_mcp_resources'
        self.assertTrue(t._allowed_paper_event(resource,'author'))
        self.assertFalse(t._allowed_paper_discovery_event(resource,resources_only=True))
        for key,value in (('server','other'),('arguments',{}),('tool','read_mcp_resource')):
            bad=copy.deepcopy(event);bad['item'][key]=value
            self.assertFalse(t._allowed_paper_event(bad,'author'))

    def test_inventory_has_no_other_user_config_servers(self):
        command=t._command('gpt-6-astra','high',None,paper_profile='author')
        self.assertIn('--ignore-user-config',command);self.assertIn('--ignore-rules',command)
        self.assertTrue(any(command[i:i+2]==['--disable','shell_tool'] for i in range(len(command))))
        self.assertIn('agents.enabled=false',command)

if __name__=='__main__':unittest.main()
