from django.forms import Form


class FormMixin(Form):
    """ 提取错误信息，把某个字段的所有错误直接放在列表中 """
    def get_errors(self):
        errors = self.errors.get_json_data()
        new_errors = []
        for key, message_dicts in errors.items():
            for message in message_dicts:
                new_errors.append(message['message'])
        return new_errors[0]