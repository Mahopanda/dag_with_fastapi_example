from typing import Any, Dict
from dag import Dag

class DataProcessor:
    def __init__(self):
        self.dag = Dag()
        self._setup_dag()

    def _setup_dag(self):
        @self.dag.node
        def categorize(input_data):
            
            if input_data['attribute'] == 'A':
                input_data["category"] = "category_A"
                return input_data
            else:
                input_data["category"] = "category_B"
                return input_data

        @self.dag.decision
        def normalize(data):
            
            normalized_value = data['value'] / 100.0
            data['value'] = normalized_value
            if normalized_value > 0.5:
                return data, 'filter_text'
            else:
                return data, 'no_filter'

        @self.dag.node
        def filter_text(data):
            data['text'] = ''.join(filter(str.isalpha, data['text']))
            return data

        @self.dag.node
        def no_filter(data):
            return data

        categorize >> normalize
        normalize >> filter_text
        normalize >> no_filter

        self.dag.update_branch_map('normalize', 'filter_text', 'no_filter')

    def process(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        try:
            result_tuple = self.dag.infer(input_data)
            last_key = list(result_tuple.keys())[-1]
            last_value = result_tuple[last_key]
            
            return last_value
        except Exception as e:
            print(f"Error: {str(e)}")
            raise ValueError(str(e))

