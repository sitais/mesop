import mesop as me


@me.stateclass
class State:
  val: int = 0


@me.on(me.ClickEvent)
def click(event: me.ClickEvent):
  state = me.state(State)
  state.val += 1


@me.page(path="/nested")
def app():
  state = me.state(State)

  with me.box(background_color="pink"):
    me.text(text="hi1")
    with me.box(background_color="blue"):
      me.text(text="hi2")
      me.button(label="a button", on_click=click, key="incredibly_long_key")
      with me.box(background_color="orange"):
        me.text(text=f"{state.val} clicks")
