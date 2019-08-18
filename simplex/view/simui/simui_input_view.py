class SIMUIInputView():

    def __init__(self):
        self.type = None
        self.name = None
        self.min_max = []

    def set_type(self, type: str):
        self.type = type

        return self

    def set_name(self, name: str):
        self.name = name

        return self

    def set_min_max(self, min_max: []):
        self.min_max = min_max

        return self

    def render(self):
        if self.type in ['number', 'date']:
            input_content = '<input name={} type={} min={} max={}>'.format(
                self.name,
                self.type,
                self.min_max[0],
                self.min_max[1]
            )
        else:
            input_content = '<input name={} type={}}>'.format(
                self.name,
                self.type
            )

        return input_content
