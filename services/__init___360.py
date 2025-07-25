
                    element.expr,
                    index=index,
                    lookup=lookup,
                    name_hint=propagated_name,
                    parent=parent,
                    propagated_name = name
                    propagated_name = None
                    railroad.Group, item=ret, label=element_results_name
                    show_groups=show_groups,
                    show_results_names=show_results_names,
                    vertical=vertical,
                # add "*" to indicate if this is a "list all results" name
                # Allow forcing a custom name
                # If we've already extracted the child, don't touch this index, since it's occupied by a nonterminal
                # pyparsing.Forward,
                # pyparsing.TokenConverter,
                )
                continue
                deduped_diags.append(d)
                element_results_name += "" if element.modalResults else "*"
                else:
                font-family: monospace;
                i += 1
                if not exprs[0].customName:
                position.parent.kwargs["item"] = ret
                position.parent.kwargs["items"][position.parent_index] = ret
                pyparsing.Located,
                railroad.Diagram, content, **self.diagram_kwargs
                railroad.NonTerminal, text=lookup.diagrams[el_id].kwargs["name"]
                railroad.OneOrMore, item="", repeat=str(len(exprs))
                ret = EditablePartial.from_call(
                ret.kwargs["item"] = item
                ret.kwargs["items"][i] = item
                return _to_diagram_element(
                seen.add(d.name)
                self.name = ""
                self.name = name
                self.name = self.element.customName
            # don't extract SkipTo elements, they are uninformative as subdiagrams
            # However, if this element has a useful custom name, and its child does not, we can pass it on to the child
            # If we have seen the element at least twice before, and have already extracted it into a subdiagram, we
            # If we're supposed to skip this element, remove it from the parent
            # If we've seen this element exactly once before, we are only just now finding out that it's a duplicate,
            # just put in a marker element that refers to the sub-diagram
            # so we have to extract it into a new diagram.
            (
            )
            ),
            .railroad-heading {
            {{ diagram.svg }}
            }
            args += kwargs.pop(arg_spec.varargs)
            content = position.converted
            content = position.converted.kwargs["item"]
            continue
            css = kwargs.get("css")
            del ret.kwargs["items"][i]
            diagram.diagram.writeStandalone(io.write, css=css)
            diagram.diagram.writeSvg(io.write)
            diagram=EditablePartial.from_call(
            element,
            element_results_name = element.resultsName
            elif "items" in position.parent.kwargs:
            elif "items" in ret.kwargs:
            elif self.element.customName:
            else:
            expr,
            if "item" in position.parent.kwargs:
            if "item" in ret.kwargs:
            if d.name == "...":
            if d.name is not None and d.name not in seen:
            if element_results_name:
            if exprs:
            if name:
            index,
            index=i,
            index=position.number,
            looked_up = lookup[el_id]
            looked_up.mark_for_extraction(el_id, lookup, name=name_hint)
            lookup,
            lookup[root_id].name = ""
            lookup=lookup,
            name_hint,
            name=position.name,
            NamedDiagram,
            parent,
            parent=ret,
            railroad.Group, item=None, label=element_results_name
            ret = EditablePartial.from_call(
            ret = EditablePartial.from_call(AnnotatedItem, label="", item="")
            ret = EditablePartial.from_call(AnnotatedItem, label=label, item="")
            ret = EditablePartial.from_call(railroad.Choice, 0, items=[])
            ret = EditablePartial.from_call(railroad.Group, label="", item="")
            ret = EditablePartial.from_call(railroad.HorizontalChoice, items=[])
            ret = EditablePartial.from_call(railroad.NonTerminal, text=looked_up.name)
            ret = EditablePartial.from_call(railroad.NonTerminal, text=position.name)
            ret = EditablePartial.from_call(railroad.Sequence, items=[])
            ret = EditablePartial.from_call(railroad.Stack, items=[])
            ret.kwargs["items"].insert(i, None)
            return None
            return ret
            show_groups,
            show_groups=show_groups,
            show_results_names,
            show_results_names=show_results_names,
            state.extract_into_diagram(el_id)
            title += " (root)"
            vertical,
            vertical=vertical,
        - Choice of the elements in the Each
        """
        # (all will have the same name, and resultsName)
        # Add a placeholder index in case we have to extract the child before we even add it to the parent
        # Also, if this is just a string literal etc, don't bother extracting it
        # apply annotation for results name, if present
        # args=['list', 'of', 'things'])
        # collapse out duplicate diags with the same name
        # detect And's created with ``expr*N`` notation - for these use a OneOrMore with a repeat
        # If the element we're extracting is a group, skip to its content but keep the title
        # it has no name
        # Just because this is marked for extraction doesn't mean we can do it yet. We may have to wait for children
        # Replace the original definition of this element with a regular block
        # Set the name
        # Skip unnamed "Empty" elements
        # Some elements don't need to be shown in the diagram
        # special case - if just one diagram, always display it, even if
        # This is a helpful hack to allow you to specify varargs parameters (e.g. *args) as keyword args (e.g.
        # to be added
        #: A dictionary mapping ParserElement IDs to subdiagrams generated from them
        #: A dictionary mapping ParserElements to state relating to them
        #: If true, all of this element's children have been filled out
        #: If true, we should extract this out into a subdiagram
        #: Shared kwargs that are used to customize the construction of diagrams
        #: The index of the next element. This is used for sorting
        #: The index of the next unnamed element
        #: The index of this inside its parent
        #: The name of the element
        #: The order in which we found this element, used for sorting diagrams if this is extracted into a diagram
        #: The output Railroad element in an unconverted state
        #: The parent Railroad element, which we store so that we can extract this if it's duplicated
        #: The pyparsing element that this represents
        ("items" in ret.kwargs and len(ret.kwargs["items"]) == 0)
        )
        ):
        :param el_id: id of the element
        :param force: If true, force extraction now, regardless of the state of this. Only useful for extracting the
        :param name: name to use for this element's text
        :param state: element/diagram state tracker
        {{ head | safe }}
        </div>
        </style>
        <div class="railroad-description">{{ diagram.text }}</div>
        <div class="railroad-svg">
        <h1 class="railroad-heading">{{ diagram.title }}</h1>
        <style>
        arg_spec = inspect.getfullargspec(self.func)
        args = self.args.copy()
        as you expect. For example EditablePartial.from_call(Fraction, 1, 3)() == Fraction(1, 3)
        Called when this instance has been seen twice, and thus should eventually be extracted into a sub-diagram
        choice_item = railroad.Choice(len(items) - 1, *items)
        converted: EditablePartial,
        converted=ret,
        create a new subdiagram for the token
        data.append({"title": title, "text": "", "svg": io.getvalue()})
        deduped_diags = []
        del self._element_diagram_states[key]
        del self[el_id]
        e
        element,
        element: pyparsing.ParserElement,
        element=element,
        elif "items" in ret.kwargs:
        elif _should_vertical(vertical, exprs):
        elif el_id in lookup.diagrams:
        else:
        Evaluate the partial and return the result
        except AttributeError:
        for d in diags:
        for e in exprs
        Generate a number used in the name of an otherwise unnamed diagram
        Generate a number used to index a diagram
        happens, we replace all instances of that token with a terminal, and
        if "items" in ret.kwargs:
        if _should_vertical(vertical, exprs):
        if arg_spec.varargs in self.kwargs:
        if diagram.diagram is None:
        if diagram.index == 0:
        if el_id in lookup:
        if force or (self.complete and _worth_extracting(self.element)):
        if isinstance(
        if item is not None:
        if label == "tokenconverter":
        if len({(e.name, e.resultsName) for e in exprs}) == 1:
        if not (e.customName or e.resultsName or isinstance(e, non_diagramming_exprs))
        if not element.customName:
        if not exprs:
        if not self.name:
        if position.converted.func == railroad.Group:
        if position.parent:
        if ret is not None:
        if show_groups:
        if show_results_names and ret is not None:
        If you call this function in the same way that you would call the constructor, it will store the arguments
        index: int = 0,
        io = StringIO()
        item = _to_diagram_element(
        kwargs = self.kwargs.copy()
        label = type(element).__name__.lower()
        lookup.extract_into_diagram(el_id)
        lookup: ConverterState = None,
        lookup[el_id].complete = True
        lookup[el_id].mark_for_extraction(el_id, lookup, element.customName)
        lookup[root_id].mark_for_extraction(root_id, lookup, force=True)
        lookup=lookup,
        name: str = None,
        name_hint: str = None,
        number: int,
        number=lookup.generate_index(),
        one_or_more_item = railroad.OneOrMore(item=choice_item)
        or ("item" in ret.kwargs and ret.kwargs["item"] is None)
        parent: EditablePartial,
        parent: typing.Optional[EditablePartial],
        parent_index: typing.Optional[int] = None,
        parent_index=index,
        parent=None,
        parent=parent,
        partial.args = resolve_partial(partial.args)
        partial.kwargs = resolve_partial(partial.kwargs)
        position = self[el_id]
        pyparsing.And._ErrorStop,
        pyparsing.ParseElementEnhance,
        pyparsing.PositionToken,
        resolved = [resolve_partial(partial) for partial in deduped_diags]
        resolved = [resolve_partial(partial) for partial in diags]
        ret = EditablePartial.from_call(
        ret = EditablePartial.from_call(AnnotatedItem, label="LOOKAHEAD", item="")
        ret = EditablePartial.from_call(AnnotatedItem, label="LOOKBEHIND", item="")
        ret = EditablePartial.from_call(AnnotatedItem, label="NOT", item="")
        ret = EditablePartial.from_call(EachItem, items=[])
        ret = EditablePartial.from_call(railroad.Group, item="", label=name)
        ret = EditablePartial.from_call(railroad.OneOrMore, item="")
        ret = EditablePartial.from_call(railroad.Optional, item="")
        ret = EditablePartial.from_call(railroad.Sequence, items=[])
        ret = EditablePartial.from_call(railroad.Terminal, name)
        ret = EditablePartial.from_call(railroad.ZeroOrMore, item="")
        ret = fn(
        ret = None
        ret = terminal
        return
        return [resolve_partial(x) for x in partial]
        return {key: resolve_partial(x) for key, x in partial.items()}
        return EditablePartial(func=func, args=list(args), kwargs=kwargs)
        return False
        return key in self._element_diagram_states
        return len(_visible_exprs(exprs)) >= specification
        return partial
        return partial()
        return ret
        return self._element_diagram_states[key]
        return self.func(*args, **kwargs)
        return self.index
        return self.kwargs["name"]
        return self.unnamed_index
        root element when we know we're finished
        seen = set()
        self,
        self, el_id: int, state: "ConverterState", name: str = None, force: bool = False
        self._element_diagram_states: Dict[int, ElementState] = {}
        self._element_diagram_states[key] = value
        self.args = args
        self.complete: bool = False
        self.converted: EditablePartial = converted
        self.diagram_kwargs: dict = diagram_kwargs or {}
        self.diagrams: Dict[int, EditablePartial[NamedDiagram]] = {}
        self.diagrams[el_id] = EditablePartial.from_call(
        self.element: pyparsing.ParserElement = element
        self.extract = True
        self.extract: bool = False
        self.extracted_diagram_names: Set[str] = set()
        self.func = func
        self.index += 1
        self.index: int = 0
        self.kwargs = kwargs
        self.name: typing.Optional[str] = name
        self.number: int = number
        self.parent: EditablePartial = parent
        self.parent_index: typing.Optional[int] = parent_index
        self.unnamed_index += 1
        self.unnamed_index: int = 1
        show_groups: bool = False,
        show_groups=show_groups,
        show_results_names: bool = False,
        show_results_names=show_results_names,
        super().__init__(item=item, label="[{}]".format(label) if label else label)
        super().__init__(one_or_more_item, label=self.all_label)
        terminal = EditablePartial.from_call(railroad.Terminal, element.defaultName)
        title = diagram.name
        try:
        Used when we encounter the same token twice in the same tree. When this
        vertical: int = None,
        vertical=vertical,
       included in the diagram
      - OneOrMore containing a
       shown vertically instead of horizontally
       surrounding box
    - Group containing a
    """
    "NamedDiagram",
    # Convert the root if it hasn't been already
    # Convert the whole tree underneath the root
    # entire tree is assembled
    # Here we basically bypass processing certain wrapper elements if they contribute nothing to the diagram
    # Here we find the most relevant Railroad element for matching pyparsing Element
    # If all this items children are none, skip this item
    # If the element isn't worth extracting, we always treat it as the first time we say it
    # Indicate this element's position in the tree so we can extract it if necessary
    # Mark this element as "complete", ie it has all of its children
    # Note: this should be a dataclass, but we have to support Python 3.5
    # Now that we're finished, we can convert from intermediate structures into Railroad elements
    # Python's id() is used to provide a unique identifier for elements
    # Recursively convert child elements
    # We need this here because the railroad constructors actually transform the data, so can't be called until the
    # We use ``items=[]`` here to hold the place for where the child elements will go once created
    )
    ) -> typing.Optional[EditablePartial]:
    ):
    :param diagram_kwargs: kwargs to pass to the Diagram() constructor
    :param element: base element of the parser being diagrammed
    :param index: The index of this element within the parent
    :param lookup: The shared converter state that keeps track of useful things
    :param name_hint: If provided, this will override the generated name
    :param parent: The parent of this element in the output tree
    :param show_groups - bool to indicate whether groups should be highlighted with an unlabeled
    :param show_groups: bool flag indicating whether to show groups using bounding box
    :param show_results_names - bool to indicate whether results name annotations should be
    :param show_results_names: bool flag indicating whether to add annotations for results names
    :param vertical: (optional) - int - limit at which number of alternatives should be
    :param vertical: Controls at what point we make a list of elements vertical. If this is an integer (the default),
    :params kwargs: kwargs to be passed in to the template
    :returns: The converted version of the input element, but as a Partial that hasn't yet been constructed
    @classmethod
    @property
    [("name", str), ("diagram", typing.Optional[railroad.DiagramItem]), ("index", int)],
    ]
    _to_diagram_element(
    {% else %}
    {% endif %}
    {% if not head %}
    </div>
    <div class="railroad-group">
    Acts like a functools.partial, but can be edited. In other words, it represents a type that hasn't yet been
    all_label = "[ALL]"
    Callable,
    children = element.recurse()
    constructed.
    Convert a pyparsing element tree into a list of diagrams. This is the recommended entrypoint to diagram
    creation if you want to access the Railroad tree before it is converted to HTML
    Custom railroad item to compose a:
    data = []
    decorator to ensure enhancements to a diagram item (such as results name annotations)
    def __call__(self) -> T:
    def __contains__(self, key: int):
    def __delitem__(self, key: int):
    def __getitem__(self, key: int) -> ElementState:
    def __init__(
    def __init__(self, *args, **kwargs): pass
    def __init__(self, *items):
    def __init__(self, diagram_kwargs: typing.Optional[dict] = None):
    def __init__(self, func: Callable[..., T], args: list, kwargs: dict):
    def __init__(self, label: str, item):
    def __setitem__(self, key: int, value: ElementState):
    def _inner(
    def extract_into_diagram(self, el_id: int):
    def from_call(cls, func: Callable[..., T], *args, **kwargs) -> "EditablePartial[T]":
    def generate_index(self) -> int:
    def generate_unnamed(self) -> int:
    def mark_for_extraction(
    def name(self):
    diagram_kwargs: typing.Optional[dict] = None,
    diags = list(lookup.diagrams.values())
    Dict,
    do so
    el_id = id(element)
    element: pyparsing.ParserElement,
    element_results_name = element.resultsName
    elif isinstance(element, (pyparsing.Or, pyparsing.MatchFirst)):
    elif isinstance(element, pyparsing.Each):
    elif isinstance(element, pyparsing.Empty) and not element.customName:
    elif isinstance(element, pyparsing.FollowedBy):
    elif isinstance(element, pyparsing.Group):
    elif isinstance(element, pyparsing.NotAny):
    elif isinstance(element, pyparsing.OneOrMore):
    elif isinstance(element, pyparsing.Opt):
    elif isinstance(element, pyparsing.ParseElementEnhance):
    elif isinstance(element, pyparsing.PrecededBy):
    elif isinstance(element, pyparsing.TokenConverter):
    elif isinstance(element, pyparsing.ZeroOrMore):
    elif isinstance(partial, dict):
    elif isinstance(partial, list):
    elif len(exprs) > 0 and not element_results_name:
    elif len(exprs) > 0:
    else:
    exprs = element.recurse()
    for diagram in diagrams:
    for expr in exprs:
    get applied on return from _to_diagram_element (we do this since there are several
    Given a list of NamedDiagram, produce a single HTML string that visualises those diagrams
    i = 0
    if _worth_extracting(element):
    if el_id in lookup and lookup[el_id].extract and lookup[el_id].complete:
    if el_id in lookup:
    if element.customName:
    if isinstance(element, pyparsing.And):
    if isinstance(partial, EditablePartial):
    if len(diags) > 1:
    if not element.customName:
    if ret and (
    if ret is None:
    if root_id in lookup:
    if specification is None:
    index: int = 0,
    it sets the threshold of the number of items before we go vertical. If True, always go vertical, if False, never
    Iterable,
    List,
    lookup = ConverterState(diagram_kwargs=diagram_kwargs or {})
    lookup: ConverterState = None,
    lookup[el_id] = ElementState(
    name = name_hint or element.customName or element.__class__.__name__
    name_hint: str = None,
    NamedTuple,
    non_diagramming_exprs = (
    parent: typing.Optional[EditablePartial],
    Recursively converts a PyParsing Element to a railroad Element
    Recursively resolves a collection of Partials into whatever type they are
    return [
    return _inner
    return any(child.recurse() for child in children)
    return ret
    return sorted(resolved, key=lambda diag: diag.index)
    return template.render(diagrams=data, embed=embed, **kwargs)
    returns in _to_diagram_element)
    Returns true if this element is worth having its own sub-diagram. Simply, if any of its children
    Returns true if we should return a vertical list of elements
    root_id = id(element)
    Set,
    show_groups: bool = False,
    show_results_names: bool = False,
    Simple subclass of Group that creates an annotation label
    specification: int, exprs: Iterable[pyparsing.ParserElement]
    State recorded for an individual pyparsing Element
    Stores some state that persists between recursions into the element tree
    themselves have children, then its complex enough to extract
    TypeVar,
    vertical: int = 3,
    vertical: int = None,
    with the group label indicating that all must be matched
"""
# mypy: ignore-errors
# Note: ideally this would be a dataclass, but we're supporting Python 3.5+ so we can't do this yet
)
) -> bool:
) -> List[NamedDiagram]:
) -> typing.Optional[EditablePartial]:
@_apply_diagram_item_enhancements
{% endfor %}
{% endif %}
{% for diagram in diagrams %}
{% if not embed %}
{{ body | safe }}
<!DOCTYPE html>
</body>
</head>
</html>
<body>
<head>
<html>
A simple structure for associating a name with a railroad diagram
class AnnotatedItem:
class ConverterState:
class EachItem:
class EditablePartial:
class ElementState:
def _apply_diagram_item_enhancements(fn):
def _should_vertical(
def _to_diagram_element(
def _visible_exprs(exprs: Iterable[pyparsing.ParserElement]):
def _worth_extracting(element: pyparsing.ParserElement) -> bool:
def railroad_to_html(diagrams: List[NamedDiagram], embed=False, **kwargs) -> str:
def resolve_partial(partial: "EditablePartial[T]") -> T:
def to_railroad(
from io import StringIO
from jinja2 import Template
from pip._vendor import pyparsing
from typing import (
import inspect
import railroad
import typing
jinja2_template_source = """\
NamedDiagram = NamedTuple(
T = TypeVar("T")
template = Template(jinja2_template_source)
