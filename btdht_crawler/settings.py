# -*- coding: utf-8 -*-
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU General Public License version 3 for
# more details.
#
# You should have received a copy of the GNU General Public License version 3
# along with this program; if not, write to the Free Software Foundation, Inc., 51
# Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#
# (c) 2015-2016 Valentin Samir
"""Default values for the app's settings"""
from django.conf import settings
from django.contrib.staticfiles.templatetags.staticfiles import static


#: URL to the logo showed in the up left corner on the default templates.
BTDHT_LOGO_URL = static("btdht_crawler/logo.png")
#: URL to the favicon (shortcut icon) used by the default templates. Default is a key icon.
BTDHT_FAVICON_URL = static("btdht_crawler/favicon.ico")
#: Show the powered by footer if set to ``True``
BTDHT_SHOW_POWERED = True
#: URLs to css and javascript external components.
BTDHT_COMPONENT_URLS = {
    "bootstrap3_css": "//maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css",
    "bootstrap3_js": "//maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min.js",
#    "fontawesome": "//maxcdn.bootstrapcdn.com/font-awesome/4.6.3/css/font-awesome.min.css",
    "html5shiv": "//oss.maxcdn.com/libs/html5shiv/3.7.0/html5shiv.js",
    "respond": "//oss.maxcdn.com/libs/respond.js/1.4.2/respond.min.js",
    "jquery": "//code.jquery.com/jquery.min.js",
}



BTDHT_MONGODB = "btdht-crawler"

BTDHT_TRACKERS = [
    "udp://tracker.leechers-paradise.org:6969/announce",
    "udp://IPv6.leechers-paradise.org:6969/announce",
    "udp://tracker.zer0day.to:1337/announce",
    "udp://tracker.coppersurfer.tk:6969/announce",

    "udp://9.rarbg.com:2710/announce",
    "udp://9.rarbg.me:2710/announce",
    "udp://9.rarbg.to:2710/announce",
    "udp://tracker.opentrackr.org:1337/announce",

    "udp://tracker.internetwarriors.net:1337/announce",
    "udp://tracker.sktorrent.net:6969/announce",
    "udp://tracker.pirateparty.gr:6969/announce",

    "udp://tracker.desu.sh:6969",
]

BTDHT_TORRENTS_BASE_PATH = "/home/admin/Programmes/openbay-crawler/transfert/btdht-crawler/torrents_done"

BTDHT_PAGE_SIZE = 25

BTDHT_SCRAPE_MIN_INTERVAL = 600

GLOBALS = globals().copy()
for name, default_value in GLOBALS.items():
    # only care about parameter begining by BTDHT_
    if name.startswith("BTDHT_"):
        # get the current setting value, falling back to default_value
        value = getattr(settings, name, default_value)
        # set the setting value to its value if defined, ellse to the default_value.
        setattr(settings, name, value)


# Allow the user defined BTDHT_COMPONENT_URLS to omit not changed values
MERGED_BTDHT_COMPONENT_URLS = BTDHT_COMPONENT_URLS.copy()
MERGED_BTDHT_COMPONENT_URLS.update(settings.BTDHT_COMPONENT_URLS)
settings.BTDHT_COMPONENT_URLS = MERGED_BTDHT_COMPONENT_URLS

