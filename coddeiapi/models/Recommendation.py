class Recommendation():

    @classmethod
    def handle_recommendation(cls, recommendation):
        recommendation['_id'] = str(recommendation['_id'])
        if 'author_id' in recommendation:
            recommendation['author_id'] = str(recommendation['author_id'])

        recommendation['created_at'] = str(recommendation['created_at'])
        return recommendation
