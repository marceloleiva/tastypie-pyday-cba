from tastypie.serializers import Serializer


class CSVSerializer(Serializer):
    formats = ['json', 'jsonp', 'xml', 'yaml', 'html', 'plist', 'csv']
    content_types = {
        'json': 'application/json',
        'jsonp': 'text/javascript',
        'xml': 'application/xml',
        'yaml': 'text/yaml',
        'html': 'text/html',
        'plist': 'application/x-plist',
        'csv': 'text/csv',
    }

    def bundle_to_csv(self, bundle):
        return ",".join(bundle.values())

    def get_header(self, bundle):
        pass

    def to_csv(self, data, options=None):
        options = options or {}
        data = self.to_simple(data, options)
        if 'objects' in data.keys():
            raw_data = ""
            for obj in data.get('objects'):
                raw_data += self.bundle_to_csv(obj)
                raw_data += "\n"
        else:
            raw_data = self.bundle_to_csv(data)
        return raw_data
