# modules/common/browsing_context_1.py

class BrowsingContext:
    def __init__(self, context_id=None, parent_id=None):
        self.context_id = context_id
        self.parent_id = parent_id
        self.children = []

    def add_child(self, child_context):
        if isinstance(child_context, BrowsingContext):
            self.children.append(child_context)

    def get_children(self):
        return self.children

    def __repr__(self):
        return (
            f"BrowsingContext(context_id={self.context_id}, "
            f"parent_id={self.parent_id}, "
            f"children={len(self.children)})"
        )
