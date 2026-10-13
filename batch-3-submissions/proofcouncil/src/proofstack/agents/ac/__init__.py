"""Author/Critic workflow — sibling of ``proofstack.agents.pwc``.

Public surface: ``ACWorkflow`` (the iterative loop) and the underlying
``Author`` / ``ACCritic`` / ``Council`` / ``Compute`` agents for direct
testing.
"""
from proofstack.agents.ac.ac_workflow import ACDAGWorkflow, ACWorkflow
from proofstack.agents.ac.visual_blocks import (
    ACInitBlock,
    ACAuthorBlock,
    ACComputeBlock,
    ACReviewJoinBlock,
    ACCompileGateBlock,
    ACReturnBlock,
    ACCouncilBlock,
    ACFreshCriticBlock,
    ACStatefulCriticBlock,
)
from proofstack.agents.ac.author import Author
from proofstack.agents.ac.compute import Compute
from proofstack.agents.ac.council import Council, CouncilMember, CouncilReply
from proofstack.agents.ac.critic import ACCritic

__all__ = [
    "ACWorkflow",
    "ACDAGWorkflow",
    "ACInitBlock",
    "ACAuthorBlock",
    "ACStatefulCriticBlock",
    "ACFreshCriticBlock",
    "ACCouncilBlock",
    "ACComputeBlock",
    "ACCompileGateBlock",
    "ACReviewJoinBlock",
    "ACReturnBlock",
    "Author",
    "ACCritic",
    "Council",
    "CouncilMember",
    "CouncilReply",
    "Compute",
]
