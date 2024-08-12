import requests

class DatabricksGenieService:

    def is_POC(self):
        return self.is_poc

    def __init__(self):
        self.api_key = "xyz_key"
        self.base_url = "https://your-databricks-instance-url/api/2.0/"
        self.is_poc = True

    def init_service(self):
        # Dummy code to connect to Databricks using API key and start AI model genie
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        endpoint = self.base_url + "start_ai_model_genie"
        
        ### In POC, won't call API
        if self.is_POC():
            print('POC env, skip API call')
        else:
            response = requests.post(endpoint, headers=headers)
            if response.status_code == 200:
                print("Databricks AI model genie started successfully.")
            else:
                print(f"Failed to start Databricks AI model genie. Status code: {response.status_code}")
        
            

    def query_service(self, query_str):
        # Dummy code to validate query_str and pass it to Databricks service
        if not isinstance(query_str, str):
            raise ValueError("query_str must be a string.")

        # Example of validating query_str (replace with actual validation logic)
        if not self.is_POC():
            if "SELECT" not in query_str.upper():
                raise ValueError("Invalid query format. Must be a SELECT statement.")

        # Example of executing the query (replace with actual Databricks API call)
        endpoint = self.base_url + "query"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        data = {
            "query": query_str
        }

        if self.is_POC():
            print('POC env, skip API call, return dummy code')
            return "We recommend you to extract below 3 fields to fufill your requirements: \nBU, Bond_ID, Market_value"
        else:
            response = requests.post(endpoint, headers=headers, json=data)
            if response.status_code == 200:
                results = response.json()["results"]
                return [str(result) for result in results]  # Convert results to list of strings
            else:
                raise RuntimeError(f"Failed to execute query: {response.status_code}, {response.text}")

"""
# Example usage:
databricks = DatabricksGenieService()
databricks.init_service()

query = "SELECT * FROM table_name"
results = databricks.query_service(query)
print("Query results:", results)


"""

if __name__ == "__main__":
    databricks = DatabricksGenieService()
    print(databricks)
    databricks.init_service()
    databricks.query_service('Hi test query string SELECT 1 from dual')
