from pathlib import Path
import os
import json
p=Path('/opt/environment/lean-path.txt')
paths=[str(Path(x).resolve()) for x in p.read_text().strip().split(':') if x]
Path('/opt/environment/unbuilt-library-paths.json').write_text(json.dumps([x for x in paths if not Path(x).is_dir()],indent=2)+'\n')
paths=[x for x in paths if Path(x).is_dir()]
assert '/opt/mathlib/.lake/build/lib/lean' in paths
p.write_text(':'.join(paths)+'\n')
Path('/opt/environment/probe-libraries.json').write_text(json.dumps(sorted(set(x for x in paths if x.endswith('/.lake/build/lib/lean'))),indent=2)+'\n')
wrapper=Path('/usr/local/bin/lean')
wrapper.write_text("#!/bin/sh\nLEAN_PATH=\"$(cat /opt/environment/lean-path.txt)\" exec /opt/lean/bin/lean \"$@\"\n")
wrapper.chmod(0o755)
