from typing import Any, Dict, Union, Optional
from ansiblelint.file_utils import Lintable

from ansiblelint.rules import AnsibleLintRule
import re


class ExampleRule(AnsibleLintRule):
    id = "10000"
    shortdesc = "Shouldn't begin 'Example' in the name."
    description = "Example custom rule."
    severity = "MEDIUM"
    tags = [""]

    def matchtask(
        self, task: Dict[str, Any], file: "Optional[Lintable]" = None
    ) -> Union[bool, str]:
        if re.search(r'Example', task['name']):
            return True

        return False
