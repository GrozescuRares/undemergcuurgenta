class BaseHelper:
    @staticmethod
    def get_unique_count(queryset, model_name, model_field):
        """
            This function returns the unique count of certain models from a query set
        """
        unique = set()
        for element in queryset:
            unique.add(getattr(getattr(element, model_name), model_field))

        return len(unique)
