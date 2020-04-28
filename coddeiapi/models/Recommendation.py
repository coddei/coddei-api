class Recommendation():

    @classmethod
    def handle_recommendation(cls, recommendation):
        recommendation['_id'] = str(recommendation['_id'])
        recommendation['author_id'] = str(recommendation['author_id'])
        return recommendation
