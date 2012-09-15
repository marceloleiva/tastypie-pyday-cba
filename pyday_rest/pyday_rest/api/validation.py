from tastypie.validation import Validation


class TwitterValidation(Validation):

    def is_valid(self, bundle, request=None):
        if len(bundle.data['tweet']) > 140:
            return {"tweet": "Tweet should have less than 140 chars."}
        return {}
