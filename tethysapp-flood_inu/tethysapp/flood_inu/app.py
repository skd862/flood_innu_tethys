from tethys_sdk.base import TethysAppBase, url_map_maker


class FloodInu(TethysAppBase):
    """
    Tethys app class for Flood Innundation SEA.
    """

    name = 'Flood Innundation SEA'
    index = 'flood_inu:home'
    icon = 'flood_inu/images/icon.gif'
    package = 'flood_inu'
    root_url = 'flood-inu'
    color = '#27AE60'
    description = 'testing'
    tags = '"Testing"'
    enable_feedback = False
    feedback_emails = []

    def url_maps(self):
        """
        Add controllers
        """
        UrlMap = url_map_maker(self.root_url)

        url_maps = (
            UrlMap(
                name='home',
                url='flood-inu',
                controller='flood_inu.controllers.home'
            ),
        )

        return url_maps