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
        start_view='decade',
        start_date='01/01/2011',
        end_date='12/31/2011',
    )

    start_date_picker = DatePicker(
        name='start_date_picker',
        display_text='Start Date Range',
        autoclose=True,
        format='mm/dd/yyyy',
        start_view='decade',
        start_date='01/01/2011',
        end_date='12/31/2011',
    )

    end_date_picker = DatePicker(
        name='end_date_picker',
        display_text='End Date Range',
        autoclose=True,
        format='mm/dd/yyyy',
        start_view='decade',
        start_date='01/01/2011',
        end_date='12/31/2011',
    )

    pick_date_range = Button(
        display_text='Choose this date range:',
        name='pick_date_range',
        style='success',
        attributes={
            'data-toggle': 'tooltip',
            'data-placement': 'top',
            'title': 'Save'
        }
    )

    context = {
        'pick_date_range': pick_date_range,
        'date_picker': date_picker,
        'start_date_picker': start_date_picker,
        'end_date_picker': end_date_picker,
    }

    return render(request, 'flood_inu/home.html', context)
