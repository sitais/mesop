from dataclasses import dataclass
from typing import Any, Callable

from pydantic import validate_arguments

import mesop.components.select.select_pb2 as select_pb
from mesop.component_helpers import (
  insert_component,
  register_event_handler,
  register_event_mapper,
)
from mesop.events import MesopEvent


@dataclass
class SelectOpenedChangeEvent(MesopEvent):
  opened: bool


register_event_mapper(
  SelectOpenedChangeEvent,
  lambda event, key: SelectOpenedChangeEvent(
    key=key,
    opened=event.bool,
  ),
)


@dataclass
class SelectSelectionChangeEvent(MesopEvent):
  value: str


register_event_mapper(
  SelectSelectionChangeEvent,
  lambda event, key: SelectSelectionChangeEvent(
    key=key,
    value=event.string,
  ),
)


@dataclass
class SelectOption:
  label: str
  value: str


@validate_arguments
def select(
  options: list[SelectOption],
  *,
  key: str | None = None,
  label: str = "",
  user_aria_described_by: str = "",
  disabled: bool = False,
  disable_ripple: bool = False,
  tab_index: float = 0,
  hide_single_selection_indicator: bool = False,
  placeholder: str = "",
  required: bool = False,
  multiple: bool = False,
  value: str = "",
  aria_label: str = "",
  aria_labelledby: str = "",
  typeahead_debounce_interval: float = 0,
  id: str = "",
  on_opened_change: Callable[[SelectOpenedChangeEvent], Any] | None = None,
  on_selection_change: Callable[[SelectSelectionChangeEvent], Any]
  | None = None,
):
  """Creates a Select component.

  Args:
    key (str|None): Unique identifier for this component instance.
    user_aria_described_by (str): Implemented as part of MatFormFieldControl. @docs-private
    disabled (bool): Whether the select is disabled.
    disable_ripple (bool): Whether ripples in the select are disabled.
    tab_index (float): Tab index of the select.
    hide_single_selection_indicator (bool): Whether checkmark indicator for single-selection options is hidden.
    placeholder (str): Placeholder to be shown if no value has been selected.
    required (bool): Whether the component is required.
    multiple (bool): Whether the user should be allowed to select multiple options.
    value (str): Value of the select control.
    aria_label (str): Aria label of the select.
    aria_labelledby (str): Input that can be used to specify the `aria-labelledby` attribute.
    typeahead_debounce_interval (float): Time to wait in milliseconds after the last keystroke before moving focus to an item.
    id (str): Unique id of the element.
    on_opened_change (Callable[[SelectOpenedChangeEvent], Any]|None): Event emitted when the select panel has been toggled.
    on_selection_change (Callable[[SelectSelectionChangeEvent], Any]|None): Event emitted when the selected value has been changed by the user.
  """
  insert_component(
    key=key,
    type_name="select",
    proto=select_pb.SelectType(
      options=[
        select_pb.SelectOption(label=option.label, value=option.value)
        for option in options
      ],
      label=label,
      user_aria_described_by=user_aria_described_by,
      disabled=disabled,
      disable_ripple=disable_ripple,
      tab_index=tab_index,
      hide_single_selection_indicator=hide_single_selection_indicator,
      placeholder=placeholder,
      required=required,
      multiple=multiple,
      value=value,
      aria_label=aria_label,
      aria_labelledby=aria_labelledby,
      typeahead_debounce_interval=typeahead_debounce_interval,
      id=id,
      on_select_opened_change_event_handler_id=register_event_handler(
        on_opened_change, event=SelectOpenedChangeEvent
      )
      if on_opened_change
      else "",
      on_select_selection_change_event_handler_id=register_event_handler(
        on_selection_change, event=SelectSelectionChangeEvent
      )
      if on_selection_change
      else "",
    ),
  )
