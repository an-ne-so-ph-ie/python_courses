"""European Rain Forecast: city x month climatology, 100 members."""
import json
import os
from datetime import datetime, timedelta

HERE = os.path.dirname(os.path.abspath(__file__))


class Agent:
    def __init__(self):
        with open(os.path.join(HERE, "rain_quantiles.json")) as f:
            self.quantiles = json.load(f)["quantiles"]

    def predict(self, request):
        issue = datetime.fromisoformat(
            request["issue_time"].replace("Z", "+00:00"))
        months = [(issue + timedelta(hours=h)).month
                  for h in request["horizons"]]
        rain = []
        for city in request["cities"]:
            by_month = self.quantiles[
                f"{city['name']}|{city['country']}"]
            rain.append([by_month[m - 1] for m in months])
        return {"rain": rain}
