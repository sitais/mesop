#########################
### COMPONENTS
#########################
from optic.components.button.button import button as button
from optic.components.checkbox.checkbox import checkbox as checkbox
from optic.components.text.text import text as text
from optic.components.box.box import box as box
# REF(//scripts/gen_component.py):insert_component_import_export

from optic.features import page as page
from optic.events import CheckboxEvent as CheckboxEvent, ClickEvent as ClickEvent
from optic.event_handler import event_handler
from optic.key import Key as Key

from optic.api import store as store, state as state

# Give a short alias for event handler since it's ubiquitous.
on = event_handler
