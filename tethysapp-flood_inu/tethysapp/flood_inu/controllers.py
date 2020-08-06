from django.shortcuts import render
from tethys_sdk.permissions import login_required
from tethys_sdk.gizmos import Button
from tethys_sdk.gizmos import DatePicker
from django.shortcuts import redirect



@login_required()
def home(request):
    """
    Controller for the app home page.
    """

    date_picker = DatePicker(
        name='date',
        display_text='Start Date',
        autoclose=True,
        format='mm/dd/yyyy',
        start_view = 'decade',
        start_date = '01/01/2011',
        end_date = '12/31/2011',
    )

    pick_date = Button(
    display_text='Choose this date:',
    name='pick_date',
    style='success',
    attributes={
        'data-toggle':'tooltip',
        'data-placement':'top',
        'title':'Save'
        }
        )

    start_date_picker = DatePicker(
        name='start_date_picker',
        display_text='Start Date Range',
        autoclose=True,
        format='mm/dd/yyyy',
        start_view = 'decade',
        start_date = '01/01/2011',
        end_date = '12/31/2011',
    )


    end_date_picker = DatePicker(
        name='end_date_picker',
        display_text='End Date Range',
        autoclose=True,
        format='mm/dd/yyyy',
        start_view = 'decade',
        start_date = '01/01/2011',
        end_date = '12/31/2011',
    )

    pick_date_range = Button(
    display_text='Choose this date range:',
    name='pick_date_range',
    style='success',
    attributes={
        'data-toggle':'tooltip',
        'data-placement':'top',
        'title':'Save'
        }
        )

    # if request.POST and 'pick_date_range' in request.POST:
    #     has_errors = False
    #
    #     # Error
    #     start_error = ''
    #     end_error = ''
    #
    #     start_range = request.POST.get('start_date_picker', None)
    #     end_range = request.POST.get('end_date_picker', None)
    #
    #     # Validate
    #     if not start_range:
    #         has_errors = True
    #         start_error = 'Required Start Date'
    #
    #     if not end_range:
    #         has_errors = True
    #         start_error = 'Required End Date'
    #
    #     if not has_errors:
    #         return redirect()






    context = {
        'pick_date': pick_date,
        'pick_date_range': pick_date_range,
        'date_picker': date_picker,
        'start_date_picker': start_date_picker,
        'end_date_picker': end_date_picker,
    }

    return render(request, 'flood_inu/home.html', context)
