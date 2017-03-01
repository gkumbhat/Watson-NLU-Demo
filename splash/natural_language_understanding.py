from watson_developer_cloud.watson_developer_cloud_service import WatsonDeveloperCloudService
# import watson_developer_cloud.natural_language_understanding.features.v1 as features

class NaturalLanguageUnderstandingV1(WatsonDeveloperCloudService):
    """
    All methods taking features use the feature classes
    from watson_developer_cloud/natural_language_understanding/features/v1
    """
    base_url = 'https://gateway.watsonplatform.net'
    default_url = '{0}/natural-language-understanding/api'.format(base_url)
    latest_version = '2017-01-23'

    def __init__(self,
                 version,
                 url=default_url,
                 username=None,
                 password=None,
                 use_vcap_services=True):
        WatsonDeveloperCloudService.__init__(
            self, 'natural-language-understanding', url,
            username, password, use_vcap_services)
        self.version = version

    def analyze(self, features, text=None, url=None, html=None,
                clean=True, xpath=None, fallback_to_raw=True,
                return_analyzed_text=False, language=None):
        """
        This is the method to call and analyze text with the supplied features
        :param features: The list of features
        :param text: Text to analyze (pick one of text, url, or html)
        :param url: url to analyze (pick one of text, url, or html)
        :param html: html to analyze (pick one of text, url, or html)
        :param clean: should the service clean the text?
        :param xpath: xpath to use for html or url
        :param fallback_to_raw:
        :param return_analyzed_text: should the analyzed
               text be returned (defaults to false)
        :param language: what language to use
        :return: dict of analyzed text
        """
        body = {
            'clean': clean,
            'fallback_to_raw': fallback_to_raw,
            'return_analyzed_text': return_analyzed_text,
            'xpath': xpath,
            'language': language,
            'text': text,
            'url': url,
            'html': html
        }

        feature_dict = {}
        for feature in features:
            feature_dict[feature.name()] = feature.toDict()
        body['features'] = feature_dict

        if text is None and html is None and url is None:
            msg = "html, text, or url must have content"
            raise ValueError(msg)

        if len(features) < 1:
            raise ValueError("Must supply at least one feature")

        return self.request(method='POST', url='/v1/analyze',
                            params={"version": self.version},
                            headers={'content-type': 'application/json'},
                            json=body,
                            accept_json=False)

class Feature(object):
    def toDict(self):
        res = {}
        if not hasattr(self, "_dataTuples"):
            return res

        for t in self._dataTuples:
            self.addKey(t[0], t[1], res)
        return res

    def name(self):
        return self._name

    def addKey(self, var, name, data_dict):
        if var is not None:
            data_dict[name] = var
        return data_dict


class Concepts(Feature):
    def __init__(self, limit=None):
        self._dataTuples = [(limit, "limit")]
        self._name = 'concepts'


class Entities(Feature):
    def __init__(self, limit=None, model=None, emotion=None, sentiment=None):
        self._dataTuples = [(limit, "limit"), (model, "model"),
                            (emotion, "emotion"), (sentiment, "sentiment")]
        self._name = 'entities'


class Keywords(Feature):
    def __init__(self, limit=None, emotion=None, sentiment=None):
        self._dataTuples = [(limit, "limit"), (emotion, "emotion"),
                            (sentiment, "sentiment")]
        self._name = 'keywords'


class Categories(Feature):
    def __init__(self):
        self._name = 'categories'


class Emotion(Feature):
    def __init__(self, document=None, targets=None):
        self._dataTuples = [(document, "document"), (targets, "targets")]
        self._name = 'emotion'


class MetaData(Feature):
    def __init__(self):
        self._name = "metadata"


class SemanticRoles(Feature):
    def __init__(self, limit=None, entities=None, keywords=None):
        self._dataTuples = [(limit, "limit"), (entities, "entities"),
                            (keywords, "keywords")]
        self._name = "semantic_roles"


class Relations(Feature):
    def __init__(self, model=None):
        self._dataTuples = [(model, "model")]
        self._name = 'relations'


class Sentiment(Feature):
    def __init__(self, document=None, targets=None):
        self._dataTuples = [(document, "document"), (targets, "targets")]
        self._name = 'sentiment'
