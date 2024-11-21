import requests


class UDPipeAnalyzer:
    def __init__(self):
        self.api_url = "https://lindat.mff.cuni.cz/services/udpipe/api/process"

    def analyze_text(self, text):

        params = {
            'tokenizer': '',
            'tagger': '',
            'parser': '',
            'model': 'ukrainian-iu-ud-2.12-230717',
            'data': text,
        }

        response = requests.post(self.api_url, data=params)

        if response.status_code == 200:
            print("TEST WORK")
            # Parse the UDPipe result
            result_text = response.json().get('result', '')
            base_forms = self._extract_base_forms(result_text)
            return base_forms
        else:
            print(f"Error: Received status code {response.status_code} from UDPipe API")
            return []

    @staticmethod
    def _extract_base_forms(result_text):

        base_forms = []
        lines = result_text.split("\n")
        for line in lines:
            if line.strip() and not line.startswith("#"):
                columns = line.split("\t")
                if len(columns) > 2:
                    base_forms.append(columns[2])
        return base_forms
