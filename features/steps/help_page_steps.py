from behave import given, when, then

@given('Open Help page for Returns')
def open_help_page(context):
    context.app.help_page.click_help()

@then('Verify help Returns page opened')
def verify_help_page_opened(context):
    context.app.help_page.verify_help_opened()

@when('Select Help topic {dd_option_value}')
def select_promotions(context, dd_option_value):
    context.app.help_page.select_promotions(dd_option_value)
    context.app.help_page.select_returns(dd_option_value)


@then('Verify help {selected_header} page opened')
def verify_hep_topic_opened(context, selected_header):
    context.app.help_page.verify_hep_topic_opened(selected_header)