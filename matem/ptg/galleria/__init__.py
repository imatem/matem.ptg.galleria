# -*- coding: utf-8 -*-

from collective.plonetruegallery.browser.views.display import BaseDisplayType
from collective.plonetruegallery.browser.views.display import jsbool
from collective.plonetruegallery.utils import createSettingsFactory
from collective.ptg.galleria import IGalleriaDisplaySettings
from plone.memoize.view import memoize
from zope.i18nmessageid import MessageFactory

_ = MessageFactory('matem.ptg.galleria')


class IMGalleriaDisplayType(BaseDisplayType):

    name = u"im_galleria"
    schema = IGalleriaDisplaySettings
    description = _(u"label_galleria_display_type",
        default=u"IM Galleria")

    js_theme_files = {
        'light': '++resource++ptg.galleria/im_light.js',
    }
    css_theme_files = {
        'light': '++resource++ptg.galleria/im_light.css',
    }

    def css(self):
        zoomsheet = ' '
        if self.settings.galleria_zoom:
            zoomsheet = """<link rel="stylesheet" type="text/css"
                         href="++resource++ptg.galleria/zoom.css" />"""
        return u"""
<link rel="stylesheet" type="text/css"
    href="%(portal_url)s/%(css_file)s" />
%(zoomsheet)s
""" % {
            'portal_url': self.portal_url,
            'css_file': self.css_theme_files[self.settings.galleria_theme],
            'zoomsheet': zoomsheet,
        }

    def javascript(self):
        return u"""
<script type="text/javascript"
    src="%(portal_url)s/++resource++ptg.galleria/galleria.js"></script>
<script type="text/javascript"
    src="%(portal_url)s/%(js_file)s"></script>
<script type="text/javascript">
(function($){
$(document).ready(function() {
    // Initialize Galleria
    $('#galleria').galleria({
        transitionSpeed: %(duration)i,
        transition: "%(transition)s",
        autoplay: %(autoplay)s,
        clicknext: true,
        showInfo: %(showInfo)s,
        lightbox: %(lightbox)s,
        carousel: %(carousel)s,
        responsive: %(responsive)s,
        carouselSteps: %(carousel_steps)s,
        trueFullscreen: true,
        thumbnails: %(thumbnails)s,
        showImagenav: %(imagenav)s,
        height: %(height)i
    });
});
})(jQuery);

</script>
""" % {
        'portal_url': self.portal_url,
        'js_file': self.js_theme_files[self.settings.galleria_theme],
        'duration': self.settings.duration,
        'transition': self.settings.galleria_transition,
        'autoplay': self.settings.timed and \
            str(self.settings.delay) or 'false',
        'showInfo': jsbool(self.settings.galleria_auto_show_info),
        'lightbox': jsbool(self.settings.galleria_lightbox),
        'carousel': jsbool(self.settings.galleria_carousel),
        'responsive': jsbool(self.settings.galleria_responsive),
        'carousel_steps': self.settings.galleria_carousel_steps,
        'imagenav': jsbool(self.settings.galleria_imagenav),
        'thumbnails': jsbool(self.settings.galleria_thumbnails),
        'height': self.settings.galleria_height,
    }

    @property
    @memoize
    def include_download_url(self):
        return self.settings.galleria_include_download_link

    def format_description(self, img):
        if not self.include_download_url:
            return img['description']
        return """%s (<a class="download" href="%s">Download</a>)""" %(
            img['description'],
            img.get('download_url', img.get('image_url')))

GalleriaSettings = createSettingsFactory(IMGalleriaDisplayType.schema)
