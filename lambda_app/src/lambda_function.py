import traceback
from typing import Dict, Any
from collector import Collector


def lambda_handler(event: Dict[str, Any], context) -> Dict[str, Any]:
    try:
        code = event.get('code', '')
        collector = Collector(code)
        response = collector.collect()
        return {'message': 'Success!', 'data': response}
    except:
        traceback.print_exc()
        return {'message': 'Error!', 'data': None}
