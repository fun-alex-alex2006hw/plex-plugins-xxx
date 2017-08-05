####################################################################################################
#                                                                                                  #
#                               (Clip/Pic)Hunter Plex Channel                                      #
#                                                                                                  #
####################################################################################################
import bookmarks
from updater import Updater
from DumbTools import DumbKeyboard

# ClipHunter
CH_TITLE = L('ch_title')
CH_PREFIX = '/video/cliphunter'
CH_BASE_URL = 'http://www.cliphunter.com'
ICON_CH = 'icon-default-ch.png'
ICON_BM_CH = 'icon-bookmarks-ch.png'
ICON_BM_ADD_CH = 'icon-add-bookmark-ch.png'
ICON_BM_REMOVE_CH = 'icon-remove-bookmark-ch.png'
ICON_VIDEO = 'icon-video.png'
ICON_SIM = 'icon-similar.png'
ICON_CAT_CH = 'icon-tags-ch.png'
ICON_LIST = 'icon-explore.png'
ICON_TV = 'icon-tv.png'
ICON_STARS = 'icon-stars.png'
ICON_PSTARS_CH = 'icon-babe-ch.png'
ICON_PLAYLIST = 'icon-playlist.png'
ICON_UPDATE_CH = 'icon-update-ch.png'
ART_CH = 'art-default-ch.jpg'
bm_ch = bookmarks.Bookmark(CH_TITLE, CH_PREFIX, ICON_BM_ADD_CH, ICON_BM_REMOVE_CH)

# PicHunter
PH_TITLE = L('ph_title')
PH_PREFIX = '/photos/pichunter'
PH_BASE_URL = 'http://www.pichunter.com'
ICON_PH = 'icon-default-ph.png'
ICON_BM_PH = 'icon-bookmarks-ph.png'
ICON_BM_ADD_PH = 'icon-add-bookmark-ph.png'
ICON_BM_REMOVE_PH = 'icon-remove-bookmark-ph.png'
ICON_PHOTO = 'icon-photo.png'
ICON_PHOTOALBUM = 'icon-photoalbum.png'
ICON_CAT_PH = 'icon-tags-ph.png'
ICON_PSTARS_PH = 'icon-babe-ph.png'
ICON_STUDIO = 'icon-studio-ph.png'
ICON_UPDATE_PH = 'icon-update-ph.png'
ART_PH = 'art-default-ph.jpg'
bm_ph = bookmarks.Bookmark(PH_TITLE, PH_PREFIX, ICON_BM_ADD_PH, ICON_BM_REMOVE_PH)

#/page/sort/all/rating/uploaded/duration/hd
SORT = [
    ('date', 'Date'), ('rel', 'Relevance'), ('views', 'Views'), ('rating', 'Rating')
    ]
RATING = [
    ('all/all', 'All'), ('all/super', 'Super High'), ('all/high', 'High'), ('all/medium', 'Medium')
    ]
DURATION = [
    ('all', 'All'), ('300', 'Short'), ('900', 'Medium'), ('1800', 'Long')
    ]
UPLOADED = [
    ('all', 'Any Time'), ('today', 'Today'), ('yesterday', 'Yesterday'), ('week', 'This Week'),
    ('month', 'This Month'), ('3months', '3 Months'), ('year', 'This Year')
    ]
CHANNELS = [
    ('alphabetical', 'A-Z'), ('recently-updated', 'Recently Updated'),
    ('most-popular', 'Most Popular'), ('top-rated', 'Top Rated'), ('most-viewed', 'Most Viewed'),
    ('video-duration', 'Video Duration')
    ]
CHANNEL_OPT = [('rating', 'Best'), ('date', 'Newest'), ('views', 'Most Views')]

####################################################################################################
def Start():
    #HTTP.CacheTime = 0
    HTTP.CacheTime = CACHE_1HOUR

####################################################################################################
@handler(CH_PREFIX, CH_TITLE, thumb=ICON_CH, art=ART_CH)
def VideoMainMenu():
    """Setup Main Menu, Includes Updater"""

    oc = ObjectContainer(title2=CH_TITLE, art=R(ART_CH), no_cache=True)

    Updater(CH_PREFIX + '/updater', oc, ICON_UPDATE_CH)

    oc.add(DirectoryObject(
        key=Callback(HDOpt, title='Explore', href='/categories/All'),
        title='Explore', thumb=R(ICON_LIST), art=R(ART_CH)
        ))
    oc.add(DirectoryObject(
        key=Callback(CategoryList, title='Categories'),
        title='Categories', thumb=R(ICON_CAT_CH), art=R(ART_CH)
        ))
    oc.add(DirectoryObject(
        key=Callback(ChannelList, title='Channels', href='/channels'),
        title='Channels', thumb=R(ICON_TV), art=R(ART_CH)
        ))
    oc.add(DirectoryObject(
        key=Callback(PopularList, title='Popular', href='/popular/ratings'),
        title='Popular', thumb=R(ICON_STARS), art=R(ART_CH)
        ))
    oc.add(DirectoryObject(
        key=Callback(PornstarOpt, title='Pornstars', href='/pornstars'),
        title='Pornstars', thumb=R(ICON_PSTARS_CH), art=R(ART_CH)
        ))
    #oc.add(DirectoryObject(key=Callback(Playlists, title='Playlists'), title='Playlists', thumb=R(ICON_PLAYLIST)))
    oc.add(DirectoryObject(
        key=Callback(ClipBookmarksMain),
        title='My Bookmarks', thumb=R(ICON_BM_CH), art=R(ART_CH)
        ))
    #oc.add(PrefsObject(title='Preferences'))
    if Client.Product in DumbKeyboard.clients:
        DumbKeyboard(CH_PREFIX, oc, ClipSearch, dktitle='Search', dkthumb=R('icon-search.png'))
    else:
        oc.add(InputDirectoryObject(
            key=Callback(ClipSearch),
            title='Search', summary='Search ClipHunter', prompt='Search for...',
            thumb=R('icon-search.png'), art=R(ART_CH)
            ))

    return oc

####################################################################################################
@handler(PH_PREFIX, PH_TITLE, thumb=ICON_PH, art=ART_PH)
def PhotoMainMenu():
    """Setup Main Menu, Includes Updater"""

    oc = ObjectContainer(title2=PH_TITLE, art=R(ART_PH), no_cache=True)

    Updater(PH_PREFIX + '/updater', oc, ICON_UPDATE_PH)

    #oc.add(DirectoryObject(
        #key=Callback(PicHome, title='Home'),
        #title='Home', thumb=R(ICON_LIST)
        #))
    oc.add(DirectoryObject(
        key=Callback(TagsList, title='Categories', href='/tags'),
        title='Categories', thumb=R(ICON_CAT_PH), art=R(ART_PH)
        ))
    oc.add(DirectoryObject(
        key=Callback(PicPornstarOpt, title='Pornstars', href='/models/all'),
        title='Pornstars', thumb=R(ICON_PSTARS_PH), art=R(ART_PH)
        ))
    oc.add(DirectoryObject(
        key=Callback(StudioOpt, title='Studios', href='/sites/all'),
        title='Studios', thumb=R(ICON_STUDIO), art=R(ART_PH)
        ))
    oc.add(DirectoryObject(key=Callback(PicBookmarksMain),
        title='My Bookmarks', thumb=R(ICON_BM_PH), art=R(ART_PH)
        ))
    #oc.add(PrefsObject(title='Preferences'))
    if Client.Product in DumbKeyboard.clients:
        DumbKeyboard(PH_PREFIX, oc, PicSearch, dktitle='Search', dkthumb=R('icon-search.png'))
    else:
        oc.add(InputDirectoryObject(
            key=Callback(PicSearch),
            title='Search', summary='Search PicHunter', prompt='Search for...',
            thumb=R('icon-search.png'), art=R(ART_PH)
            ))

    return oc

####################################################################################################
@route(CH_PREFIX + '/validateprefs')
def ValidatePrefs():
    """
    Validate Prefs
    No Prefs to validate yet
    """

####################################################################################################
@route(CH_PREFIX + '/categorylist')
def CategoryList(title):
    """Setup Category List"""

    oc = ObjectContainer(title2=title, art=R(ART_CH))
    url = CH_BASE_URL + '/categories/'
    html = HTML.ElementFromURL(url)
    cat_list = []
    for node in html.xpath('//div/a[contains(@href, "categories")]'):
        href = node.get('href').replace(' ', '%20')
        name = node.get('title').strip()
        img = node.xpath('./img/@src')[0]
        if (name != 'All') and ((name, href, img) not in cat_list):
            cat_list.append((name, href, img))
    for (n, h, i) in sorted(cat_list):
        oc.add(DirectoryObject(
            key=Callback(HDOpt, title='Category / %s' %n, href=h),
            title=n, thumb=i, art=R(ART_CH)
            ))
    return oc

####################################################################################################
@route(PH_PREFIX + '/tags/list')
def TagsList(title, href):
    """Setup Tags List"""

    oc = ObjectContainer(title2=title, art=R(ART_PH))
    html = HTML.ElementFromURL(PH_BASE_URL + href)
    tag_list = []
    for node in html.xpath('//div/a[contains(@href, "tags")]'):
        phref = node.get('href').replace(' ', '%20')
        name = node.get('title').strip()
        if (name != 'All') and ((name, phref) not in tag_list):
            tag_list.append((name, phref))
    for (n, h) in sorted(tag_list):
        oc.add(DirectoryObject(
            key=Callback(Tag, title='Category / %s' %n, href=h),
            title=n, art=R(ART_PH)
            ))
    return oc

####################################################################################################
@route(PH_PREFIX + '/tag')
def Tag(title, href):
    """Photos in tag"""

    oc = ObjectContainer(title2=title, art=R(ART_PH))
    html = HTML.ElementFromURL(PH_BASE_URL + href)
    nextpg = nextpg_href(html)
    for (n, t, h) in pichunter_list(html):
        oc.add(DirectoryObject(
            key=Callback(PhotoAlbumOpt, title='%s / %s' %(title, n), href=h, thumb=t),
            title=n, thumb=t, art=R(ART_PH)
            ))
    if nextpg:
        oc.add(NextPageObject(
            key=Callback(Tag, title=title, href=nextpg),
            title='Next Page>>', art=R(ART_PH)
            ))
    return oc

####################################################################################################
@route(CH_PREFIX + '/hd-opt')
def HDOpt(title, href):
    """
    Default, Channels
    All, HD
    """

    oc = ObjectContainer(title2=title, art=R(ART_CH))
    oc.add(DirectoryObject(
        key=Callback(DirectoryList, title='%s / Default' %title, href=href, page=1),
        title='Default (Site Default List)', art=R(ART_CH)
        ))
    if 'Channels' in title:
        oc.add(DirectoryObject(
            key=Callback(ChannelOpt, title='%s / All' %title, href=href, hd=0),
            title='All (SD & HD)', art=R(ART_CH)
            ))
        oc.add(DirectoryObject(
            key=Callback(ChannelOpt, title='%s / HD' %title, href=href, hd=1),
            title='HD (HD Only)', art=R(ART_CH)
            ))
    else:
        oc.add(DirectoryObject(
            key=Callback(SortBy, title='%s / All' %title, href=href, hd=0),
            title='All (SD & HD)', art=R(ART_CH)
            ))
        oc.add(DirectoryObject(
            key=Callback(SortBy, title='%s / HD' %title, href=href, hd=1),
            title='HD (HD Only)', art=R(ART_CH)
            ))
    return oc

####################################################################################################
@route(CH_PREFIX + '/sortby')
def SortBy(title, href, hd):
    """Sort By (Date, Relevance, Views, Rating)"""

    oc = ObjectContainer(title2=title, art=R(ART_CH))
    for h, s in SORT:
        oc.add(DirectoryObject(
            key=Callback(Rating, title='%s / %s' %(title, s), href='%s/1/%s' %(href, h), hd=hd),
            title=s, art=R(ART_CH)
            ))
    return oc

####################################################################################################
@route(CH_PREFIX + '/rating')
def Rating(title, href, hd):
    """Rating (All, Super High, High, Medium)"""

    oc = ObjectContainer(title2=title, art=R(ART_CH))
    for h, s in RATING:
        oc.add(DirectoryObject(
            key=Callback(Uploaded, title='%s / %s' %(title, s), href='%s/%s' %(href, h), hd=hd),
            title=s, art=R(ART_CH)
            ))
    return oc

####################################################################################################
@route(CH_PREFIX + '/uploaded')
def Uploaded(title, href, hd):
    """Uploaded (Any Time, Today, Yesterday, This Week, This Month, 3 Months, This Year)"""

    oc = ObjectContainer(title2=title, art=R(ART_CH))
    for h, s in UPLOADED:
        oc.add(DirectoryObject(
            key=Callback(Duration, title='%s / %s' %(title, s), href='%s/%s' %(href, h), hd=hd),
            title=s, art=R(ART_CH)
            ))
    return oc

####################################################################################################
@route(CH_PREFIX + '/duration')
def Duration(title, href, hd):
    """Duration (All, Short, Medium, Long)"""

    oc = ObjectContainer(title2=title, art=R(ART_CH))
    for h, s in DURATION:
        oc.add(DirectoryObject(
            key=Callback(DirectoryList, title='%s / %s' %(title, s), href='%s/%s/%s' %(href, h, hd), page=1),
            title=s, art=R(ART_CH)
            ))
    return oc

####################################################################################################
@route(CH_PREFIX + '/channel/list')
def ChannelList(title, href):
    """Recently Updated, Most Popular, Top Rated, Most Viewed, A-Z"""

    oc = ObjectContainer(title2=title, art=R(ART_CH))
    for h, s in CHANNELS:
        if h != 'alphabetical':
            oc.add(DirectoryObject(
                key=Callback(Channels, title='%s / %s' %(title, s), href='%s/%s' %(href, h)),
                title=s, art=R(ART_CH)
                ))
        else:
            oc.add(DirectoryObject(
                key=Callback(Alphabetical, title='%s / A-Z' %title, href='%s/alphabetical' %href),
                title='A-Z', art=R(ART_CH)
                ))
    return oc

####################################################################################################
@route(CH_PREFIX + '/abc')
def Alphabetical(title, href):
    """All, A-Z"""

    oc = ObjectContainer(title2=title, art=R(ART_CH))
    if 'channels' in href:
        oc.add(DirectoryObject(
            key=Callback(Channels, title='%s / All' %title, href=href),
            title='All', art=R(ART_CH)
            ))
        for c in ['#'] + abc():
            oc.add(DirectoryObject(
                key=Callback(
                    Channels, title='%s / %s' %(title, c),
                    href='%s/1/%s' %(href, c.lower() if c != '#' else '1')),
                title=c, art=R(ART_CH)
                ))
    else:
        oc.add(DirectoryObject(
            key=Callback(PornstarList, title='%s / All' %title, href=href),
            title='All', art=R(ART_CH)
            ))
        for c in abc():
            oc.add(DirectoryObject(
                key=Callback(
                    PornstarList, title='%s / %s' %(title, c),
                    href='%s/%s/overview' %(href, c.lower())),
                title=c, art=R(ART_CH)
                ))
    return oc

####################################################################################################
@route(CH_PREFIX + '/channels')
def Channels(title, href):
    """List channels"""

    oc = ObjectContainer(title2=title, art=R(ART_CH))
    html = HTML.ElementFromURL(CH_BASE_URL + href)
    nextpg = nextpg_href(html)
    for node in html.xpath('//ul[@class="moviethumbs bigthumbs channelList resizable ignoreViewSwitch"]/li'):
        anode = node.xpath('./a[@class="chtl"]')[0]
        chref = anode.get('href')
        name = anode.text

        bthumb = node.xpath('./a[@class="t"]/img/@src')[0]
        athumb = node.xpath('./a[@class="chtlgx"]/img/@src')[0]

        sum_string = []
        for s in node.xpath('./a[@class="chtlgx"]/b'):
            sum_string.append(s.text)
        summary = ' | '.join([s for s in sum_string])

        oc.add(DirectoryObject(
            key=Callback(HDOpt, title='%s / %s' %(title, name), href=chref),
            title=name, thumb=athumb if athumb else bthumb, art=R(ART_CH)
            ))
    if nextpg:
        oc.add(NextPageObject(
            key=Callback(Channels, title=title, href=nextpg),
            title='Next Page>>', art=R(ART_CH)
            ))

    return oc

####################################################################################################
@route(CH_PREFIX + '/channel/opt')
def ChannelOpt(title, href, hd):
    """Best, Newest, Most Views"""

    oc = ObjectContainer(title2=title, art=R(ART_CH))
    for h, s in CHANNEL_OPT:
        oc.add(DirectoryObject(
            key=Callback(DirectoryList, title='%s / %s' %(title, s), href='%s/1/%s/%s' %(href, h, hd), page=1),
            title=s, art=R(ART_CH)
            ))
    return oc

####################################################################################################
@route(CH_PREFIX + '/popular')
def PopularList(title, href):
    """Today, Yesterday, Week, Month, Year, Hall of Fame"""

    oc = ObjectContainer(title2=title, art=R(ART_CH))
    plist = ['Today', 'Yesterday', 'Week', 'Month', 'Year', 'Hall of Fame']
    for s in plist:
        oc.add(DirectoryObject(
            key=Callback(DirectoryList,
                title='%s / %s' %(title, s),
                href='%s/%s/1' %(href, s.lower() if s != 'Hall of Fame' else 'all'), page=1),
            title=s, art=R(ART_CH)
            ))
    return oc

####################################################################################################
@route(CH_PREFIX + '/pornstar/opt')
def PornstarOpt(title, href):
    """Ratings, Followers, A-Z"""

    oc = ObjectContainer(title2=title, art=R(ART_CH))
    pslist = [('top', 'Ratings'), ('mostfollowed', 'Followers')]
    oc.add(DirectoryObject(
        key=Callback(Alphabetical, title='%s / A-Z' %title, href=href),
        title='A-Z', art=R(ART_CH)
        ))
    for (h, s) in pslist:
        oc.add(DirectoryObject(
            key=Callback(PornstarList, title='%s / %s' %(title, s), href='%s/%s' %(href, h)),
            title=s, art=R(ART_CH)
            ))
    return oc

####################################################################################################
@route(PH_PREFIX + '/pornstar/opt')
def PicPornstarOpt(title, href):
    """Pichunter: Trending, Superstars, A-Z"""

    oc = ObjectContainer(title2=title, art=R(ART_PH))
    pslist = ['trending', 'superstars']
    oc.add(DirectoryObject(
        key=Callback(PicABC, title='%s / A-Z' %title, href=href),
        title='A-Z', art=R(ART_PH)
        ))
    for s in pslist:
        oc.add(DirectoryObject(
            key=Callback(PicPornstarList, title='%s / %s' %(title, s.title()), href='%s/%s' %(href, s)),
            title=s.title(), art=R(ART_PH)
            ))
    return oc

####################################################################################################
@route(PH_PREFIX + '/pornstar/abc')
def PicABC(title, href):
    """Pornstar ABC list"""

    oc = ObjectContainer(title2=title, art=R(ART_PH))
    for c in abc():
        oc.add(DirectoryObject(
            key=Callback(PicPornstarList, title='%s / %s' %(title, c), href='%s/%s' %(href, c.lower())),
            title=c, art=R(ART_PH)
            ))
    return oc

####################################################################################################
@route(CH_PREFIX + '/pornstar/list')
def PornstarList(title, href):
    """List Pornstars"""

    oc = ObjectContainer(title2=title, art=R(ART_CH))
    html = HTML.ElementFromURL(CH_BASE_URL + href)
    nextpg = nextpg_href(html)
    for node in html.xpath('//div[@class="paper paperSpacings xs-fullscreen photoGrid"]/a'):
        phref = node.get('href')
        thumb = node.xpath('./img/@src')[0]
        name = node.xpath('./div/span/text()')[0]

        oc.add(DirectoryObject(
            key=Callback(PornstarCH, title='%s / %s' %(title, name), href=phref, thumb=thumb),
            title=name, thumb=Resource.ContentsOfURLWithFallback(thumb, 'icon-babe-miss.png'),
            art=R(ART_CH)
            ))
    if nextpg:
        oc.add(NextPageObject(
            key=Callback(PornstarList, title=title, href=nextpg),
            title='Next Page>>', art=R(ART_CH)
            ))
    return oc

####################################################################################################
@route(CH_PREFIX + '/pornstar')
def PornstarCH(title, href, thumb):
    """Videos, Photos"""

    html = HTML.ElementFromURL(CH_BASE_URL + href)

    bm_title = title.split('/')[-1].strip()
    bm_id = bm_title.lower().replace(' ', '_')
    ps_error = html.xpath('//meta[@name="canonical"]/@content')[0]
    match = bm_ch.bookmark_exist(item_id=bm_id, category='ClipPornstar')
    header = None
    message = None

    if 'search' in ps_error:
        if match:
            header = title
            message = 'Pornstar Removed from site'
        else:
            return bm_ch.message_container('Warning', 'Pornstar Not Found')

    oc = ObjectContainer(title2=title, header=header, message=message, art=R(ART_CH), no_cache=True)

    if not 'search' in ps_error:
        oc.add(DirectoryObject(
            key=Callback(HDOpt, title='%s / Videos' %title, href='%s/movies' %href),
            title='Videos', thumb=R(ICON_VIDEO), art=R(ART_CH)
            ))
        oc.add(DirectoryObject(
            key=Callback(PhotoAlbumList,
                title='%s / Photos' %title,
                href='%s/photos/1' %href.replace('pornstars', 'models')),
            title='Photos', thumb=R(ICON_PHOTO), art=R(ART_PH)
            ))
        oc.add(DirectoryObject(
            key=Callback(PornstarCHSimilar, title='%s / Similar' %title, href=href),
            title='Similar Pornstars', thumb=R(ICON_SIM), art=R(ART_CH)
            ))

    if not thumb:
        html = HTML.ElementFromURL(CH_BASE_URL + href)
        thumb = html.xpath('//img[@id="modelpic"]/@src')[0]
    bm_ch.add_remove_bookmark(
        oc=oc, title=bm_title, thumb=thumb, url=href, item_id=bm_id,
        category='ClipPornstar', duration=None, tagline=None
        )

    return oc

####################################################################################################
@route(CH_PREFIX + '/pornstar/similar')
def PornstarCHSimilar(title, href):
    """List simialr pornstars"""

    oc = ObjectContainer(title2=title, art=R(ART_CH))
    html = HTML.ElementFromURL(CH_BASE_URL + href)
    for node in html.xpath('//div[@class="links"]'):
        simnode = node.xpath('./div[@class="frontpageCatTable"]')[0]
        for node2 in simnode.xpath('.//a'):
            phref = node2.get('href')
            thumb = node2.get('data-ps-thumb')
            name = node2.text
            oc.add(DirectoryObject(
                key=Callback(PornstarCH,
                    title='%s / %s' %(title.rsplit('/', 2)[0], name),
                    href=phref, thumb=thumb),
                title=name, thumb=thumb, art=R(ART_CH)
                ))
    if len(oc) > 0:
        return oc
    else:
        return bm_ch.message_container('Similar Pornstar', 'Similar Pornstar list Empty')

####################################################################################################
@route(PH_PREFIX + '/pornstar/list')
def PicPornstarList(title, href):
    """PicHunter list pornstars"""

    oc = ObjectContainer(title2=title, art=R(ART_PH))
    html = HTML.ElementFromURL(PH_BASE_URL + href)
    nextpg = nextpg_href(html)
    for (n, t, h) in pichunter_list(html):
        oc.add(DirectoryObject(
            key=Callback(PornstarPH, title='%s / %s' %(title, n), href=h, thumb=t),
            title=n, thumb=Resource.ContentsOfURLWithFallback(t, 'icon-babe-miss.png'),
            art=R(ART_PH)
            ))
    if nextpg:
        oc.add(NextPageObject(
            key=Callback(PicPornstarList, title=title, href=nextpg),
            title='Next Page>>', art=R(ART_PH)
            ))
    return oc

####################################################################################################
@route(PH_PREFIX + '/pornstar')
def PornstarPH(title, href, thumb):
    """Videos, Photos"""

    req = HTTP.Request(PH_BASE_URL + href + '/info')
    html = HTML.ElementFromString(req.content)

    bm_title = title.split('/')[-1].strip()
    bm_id = bm_title.lower().replace(' ', '_')
    ps_removed = Regex(r'Pornstar Not Found').search(req.content)
    match = bm_ph.bookmark_exist(item_id=bm_id, category='PicPornstar')
    header = None
    message = None

    if ps_removed:
        if match:
            header = title
            message = 'Pornstar Removed from site'
        else:
            return bm_ph.message_container('Warning', 'Pornstar Not Found')

    oc = ObjectContainer(title2=title, header=header, message=message, art=R(ART_PH), no_cache=True)

    if not ps_removed:
        chpstar_href = '%s/movies' %href.replace('_', '+').replace('models', 'pornstars')
        chpstar_page = HTTP.Request(CH_BASE_URL + chpstar_href).content
        if not Regex(r'Not enough results matched your filters').search(chpstar_page):
            oc.add(DirectoryObject(
                key=Callback(HDOpt, title='%s / Videos' %title, href=chpstar_href),
                title='Videos', thumb=R(ICON_VIDEO), art=R(ART_CH)
                ))
        oc.add(DirectoryObject(
            key=Callback(PhotoAlbumList, title=title, href='%s/photos' %href),
            title='Photos', thumb=R(ICON_PHOTO), art=R(ART_PH)
            ))
        wfts = html.xpath('//b[starts-with(text(), "Worked for these Studios")]')
        if wfts:
            oc.add(DirectoryObject(
                key=Callback(PornstarPHR, title='Worked for these Studios', href=href+'/info'),
                title='Worked for these Studios', thumb=R(ICON_STUDIO), art=R(ART_PH)
                ))
        pal = html.xpath('//b[starts-with(text(), "People also like")]')
        if pal:
            oc.add(DirectoryObject(
                key=Callback(PornstarPHR, title='People also like', href=href+'/info'),
                title='People also like', thumb=R(ICON_PSTARS_PH), art=R(ART_PH)
                ))
        sww = html.xpath('//b[starts-with(text(), "She worked with")]')
        if sww:
            oc.add(DirectoryObject(
                key=Callback(PornstarPHR, title='She worked with', href=href+'/info'),
                title='She worked with', thumb=R(ICON_PSTARS_PH), art=R(ART_PH)
                ))

    if not thumb:
        html = HTML.ElementFromURL(CH_BASE_URL + href)
        thumb = html.xpath('//link[@rel="image_src"]/@href')[0]
    bm_ph.add_remove_bookmark(
        oc=oc, title=bm_title, thumb=thumb, url=href, item_id=bm_id,
        category='PicPornstar', duration=None, tagline=None
        )

    return oc

####################################################################################################
@route(PH_PREFIX + '/pornstar/related')
def PornstarPHR(title, href):
    """list related pornstars"""

    oc = ObjectContainer(title2=title, art=R(ART_PH))
    html = HTML.ElementFromURL(PH_BASE_URL + href)
    rhtml = html.xpath('//b[starts-with(text(), "%s")]' %title)[0]
    if title == "Worked for these Studios":
        slist = rhtml.getparent().getparent().getnext().xpath('./div[@class="list-group"]/a')
        for g in slist:
            stitle = g.get('title')
            shref = g.get('href')
            oc.add(DirectoryObject(
                key=Callback(Studio, title=stitle, href=shref),
                title=stitle, thumb=R(ICON_STUDIO), art=R(ART_PH)
                ))
    else:
        nhtml = rhtml.getparent().getparent().getnext().xpath('./div[@class="thumbtable"]')[0]
        for (n, t, h) in pichunter_list(nhtml, relative=True):
            oc.add(DirectoryObject(
                key=Callback(PornstarPH, title='%s / %s' %(title, n), href=h, thumb=t),
                title=n, thumb=Resource.ContentsOfURLWithFallback(t, 'icon-babe-miss.png'),
                art=R(ART_PH)
                ))
    return oc

####################################################################################################
@route(PH_PREFIX + '/studio/opt')
def StudioOpt(title, href):
    """All, #, A-Z"""

    oc = ObjectContainer(title2=title, art=R(ART_PH))
    oc.add(DirectoryObject(
        key=Callback(StudioList, title='%s / All' %title, href=href + '/everything/1'),
        title='All', art=R(ART_PH)
        ))
    for c in ['#'] + abc():
        oc.add(DirectoryObject(
            key=Callback(StudioList,
                title='%s / %s' %(title, c),
                href='%s/%s/1' %(href, c.lower() if c != '#' else '0')),
            title=c, art=R(ART_PH)
            ))
    return oc

####################################################################################################
@route(PH_PREFIX + '/studio/list')
def StudioList(title, href):
    """List Studios"""

    oc = ObjectContainer(title2=title, art=R(ART_PH))
    html = HTML.ElementFromURL(PH_BASE_URL + href)
    nextpg = nextpg_href(html)
    for (n, t, h) in pichunter_list(html):
        oc.add(DirectoryObject(
            key=Callback(Studio, title='%s / %s' %(title, n), href=h),
            title=n, thumb=t, art=R(ART_PH)
            ))
    if nextpg:
        oc.add(NextPageObject(
            key=Callback(StudioList, title=title, href=nextpg),
            title='Next Page>>', art=R(ART_PH)
            ))
    if len(oc) > 0:
        return oc
    else:
        return bm_ph.message_container('Studio list', 'Stuido list Empty')

####################################################################################################
@route(PH_PREFIX + '/studio')
def Studio(title, href):
    """List Albums in Studio"""

    oc = ObjectContainer(title2=title, art=R(ART_PH))
    html = HTML.ElementFromURL(PH_BASE_URL + href)
    nextpg = nextpg_href(html)
    for (n, t, h) in pichunter_list(html):
        oc.add(DirectoryObject(
            key=Callback(PhotoAlbumOpt, title='%s / %s' %(title, n), href=h, thumb=t),
            title=n, thumb=t, art=R(ART_PH)
            ))
    if nextpg:
        oc.add(NextPageObject(
            key=Callback(Studio, title=title, href=nextpg),
            title='Next Page>>', art=R(ART_PH)
            ))
    return oc

####################################################################################################
@route(PH_PREFIX + '/pornstar/photoalbumlist')
def PhotoAlbumList(title, href):
    """List Photo Albums for Pornstar"""

    oc = ObjectContainer(title2=title, art=R(ART_PH))
    html = HTML.ElementFromURL(PH_BASE_URL + href)
    nextpg = nextpg_href(html)
    for (n, t, h) in pichunter_list(html):
        oc.add(DirectoryObject(
            key=Callback(PhotoAlbumOpt, title='%s / %s' %(title, n), href=h, thumb=t),
            title=n, thumb=t, art=R(ART_PH)
            ))
    if nextpg:
        oc.add(NextPageObject(
            key=Callback(PhotoAlbumList, title=title, href=nextpg),
            title='Next Page>>', art=R(ART_PH)
            ))
    if len(oc) > 0:
        return oc
    else:
        ntitle = title.split('/')[-2].strip()
        return bm_ph.message_container('Photo Album list', '%s Photo Album list Empty' %ntitle)

####################################################################################################
@route(CH_PREFIX + '/search')
def ClipSearch(query=''):
    """Search ClipHunter"""

    href = '/search/%s' %String.Quote(query.strip(), usePlus=True)
    title = 'Search / %s' %query

    oc = ObjectContainer(title2=title, art=R(ART_CH))
    data = JSON.ObjectFromURL(CH_BASE_URL + '/a/autocomplete?type=model&txt=%s' %String.Quote(query.strip(), usePlus=False))
    if len(data) > 0:
        oc.add(DirectoryObject(
            key=Callback(CHPSearch, query=query.strip(), data=data),
            title='Pornstars', thumb=R(ICON_PSTARS_CH), art=R(ART_CH)
            ))
        oc.add(DirectoryObject(
            key=Callback(HDOpt, title=title, href=href),
            title='Videos', thumb=R(ICON_VIDEO), art=R(ART_CH)
            ))
        return oc
    else:
        return HDOpt(title, href)

####################################################################################################
@route(CH_PREFIX + '/pornstar/search', data=list)
def CHPSearch(query, data):

    if len(data) == 1:
        t = data[0]
        h = '/pornstars/%s' %String.Quote(t, usePlus=True)
        thumb = HTTP.Request(CH_BASE_URL + '/a/modelthumb?name=%s' %String.Quote(t, usePlus=True)).content
        return PornstarCH(t, h, thumb)
    else:
        oc = ObjectContainer(title2='Search / %s' %query, art=R(ART_CH))
        for d in data:
            h = '/pornstars/%s' %String.Quote(d, usePlus=True)
            thumb = HTTP.Request(CH_BASE_URL + '/a/modelthumb?name=%s' %String.Quote(d, usePlus=True)).content
            oc.add(DirectoryObject(
                key=Callback(PornstarCH, title=d, href=h, thumb=thumb), title=d,
                thumb=thumb, art=R(ART_CH)
                ))
        return oc

####################################################################################################
@route(PH_PREFIX + '/search')
def PicSearch(query=''):
    """Search PicHunter"""

    href = '/search/%s/1' %String.Quote(query.strip(), usePlus=True)
    title = 'Search / %s' %query

    oc = ObjectContainer(title2=title, art=R(ART_PH))
    data = JSON.ObjectFromURL(PH_BASE_URL + '/a/autocomplete?type=model&txt=%s' %String.Quote(query.strip(), usePlus=False))
    if len(data) > 0:
        oc.add(DirectoryObject(
            key=Callback(PHPSearch, query=query.strip(), data=data),
            title='Pornstars', thumb=R(ICON_PSTARS_PH), art=R(ART_PH)
            ))
        oc.add(DirectoryObject(
            key=Callback(PicSortBy, title=title, href=href),
            title='Videos', thumb=R(ICON_PHOTO), art=R(ART_PH)
            ))
        return oc
    else:
        return PicSortBy(title, href)

####################################################################################################
@route(PH_PREFIX + '/pornstar/search', data=list)
def PHPSearch(query, data):

    if len(data) == 1:
        t = data[0]
        h = '/models/%s' %String.Quote(t, usePlus=True)
        thumb = HTTP.Request(CH_BASE_URL + '/a/modelthumb?name=%s' %String.Quote(t, usePlus=True)).content
        return PornstarPH(t, h, thumb)
    else:
        oc = ObjectContainer(title2='Search / %s' %query, art=R(ART_PH))
        for d in data:
            h = '/models/%s' %String.Quote(d, usePlus=True)
            thumb = HTTP.Request(CH_BASE_URL + '/a/modelthumb?name=%s' %String.Quote(d, usePlus=True)).content
            oc.add(DirectoryObject(
                key=Callback(PornstarPH, title=d, href=h, thumb=thumb), title=d,
                thumb=thumb, art=R(ART_PH)
                ))
        return oc

####################################################################################################
@route(PH_PREFIX + '/search/sortby')
def PicSortBy(title, href):
    """Date, Relevancy, Rating"""

    oc = ObjectContainer(title2=title + ' / Sort By:', art=R(ART_PH))
    sort_list = [('rel', 'Relevancy'), ('date', 'Date'), ('rate', 'Rating')]
    for (h, s) in sort_list:
        oc.add(DirectoryObject(
            key=Callback(PicQuality, title='%s / %s' %(title, s), href='%s/%s' %(href, h)),
            title=s, art=R(ART_PH)
            ))
    return oc

####################################################################################################
@route(PH_PREFIX + '/search/quality')
def PicQuality(title, href):
    """All, HD"""

    oc = ObjectContainer(title2=title + ' / Quality:', art=R(ART_PH))
    oc.add(DirectoryObject(
        key=Callback(PicFreshness, title='%s / All' %title, href=href + '/all'),
        title='All', art=R(ART_PH)
        ))
    oc.add(DirectoryObject(
        key=Callback(PicFreshness, title='%s / HQ Only' %title, href=href + '/hq'),
        title='HQ Only', art=R(ART_PH)
        ))
    return oc

####################################################################################################
@route(PH_PREFIX + '/search/freshness')
def PicFreshness(title, href):
    """Any Time, Today, This Week, This Month, Past 3 Months, This Year"""

    oc = ObjectContainer(title2=title + ' / Freshness:', art=R(ART_PH))
    freshness_list = [
            ('today', 'Today'), ('yesterday', 'This Week'), ('month', 'This Month'),
            ('3months', 'Past 3 Months'), ('year', 'This Year')]
    oc.add(DirectoryObject(
        key=Callback(PhotoAlbumList, title='%s / Any Time' %title, href=href),
        title='Any Time', art=R(ART_PH)
        ))
    for (h, s) in freshness_list:
        oc.add(DirectoryObject(
            key=Callback(PhotoAlbumList, title='%s / %s' %(title, s), href='%s/%s' %(href, h)),
            title=s, art=R(ART_PH)
            ))
    return oc

####################################################################################################
@route(CH_PREFIX + '/bookmarks/main')
def ClipBookmarksMain():
    """
    Setup Bookmark Main Menu.
    Seperate by Pornstar and Video
    """

    bm = Dict['Bookmarks']
    if not bm:
        return bm_ph.message_container('Bookmarks', 'Bookmarks list Empty')

    oc = ObjectContainer(title2='My Bookmarks', art=R(ART_CH), no_cache=True)

    for key in sorted(bm.keys()):
        if len(bm[key]) == 0:
            del Dict['Bookmarks'][key]
            Dict.Save()
        else:
            if key == 'ClipPornstar':
                oc.add(DirectoryObject(
                    key=Callback(ClipBookmarksSub, category=key),
                    title='Pornstars', summary='Display Pornstar Bookmarks',
                    thumb=R(ICON_PSTARS_CH), art=R(ART_CH)
                    ))
            elif key == 'Video':
                oc.add(DirectoryObject(
                    key=Callback(ClipBookmarksSub, category=key),
                    title='Videos', summary='Display Video Bookmarks',
                    thumb=R(ICON_VIDEO), art=R(ART_CH)
                    ))

    if len(oc) > 0:
        return oc
    else:
        return bm_ch.message_container('Bookmarks', 'Bookmark list Empty')

####################################################################################################
@route(CH_PREFIX + '/bookmarks/sub')
def ClipBookmarksSub(category):
    """List Bookmarks Alphabetically"""

    bm = Dict['Bookmarks']
    if not category in bm.keys():
        return bm_ph.message_container('Error',
            '%s Bookmarks list is dirty, or no %s Bookmark list exist.' %(category, category))

    oc = ObjectContainer(title2='My Bookmarks | %s' %category, art=R(ART_CH), no_cache=True)

    for bookmark in sorted(bm[category], key=lambda k: k['title']):
        title = bookmark['title']
        thumb = bookmark['thumb']
        url = bookmark['url']
        category = bookmark['category']
        vid = bookmark['id']
        duration = bookmark['duration']
        tagline = bookmark['tagline']

        if category == 'ClipPornstar':
            oc.add(DirectoryObject(
                key=Callback(PornstarCH, title=title, href=url, thumb=thumb),
                title=title, thumb=Resource.ContentsOfURLWithFallback(thumb, 'icon-babe-miss.png'),
                art=R(ART_CH)
                ))
        elif category == 'Video':
            video_info = {
                'id': vid, 'title': title, 'duration': int(duration),
                'tagline': tagline, 'thumb': thumb, 'url': url
                }
            oc.add(DirectoryObject(
                key=Callback(VideoPage, video_info=video_info),
                title=title, thumb=thumb, art=R(ART_CH)
                ))

    if len(oc) > 0:
        return oc
    else:
        return bm_ch.message_container('Bookmarks', '%s Bookmarks list Empty' %category)

####################################################################################################
@route(PH_PREFIX + '/bookmarks/main')
def PicBookmarksMain():
    """
    Setup Bookmark Main Menu.
    Seperate by Pornstar and Video/Pic
    """

    bm = Dict['Bookmarks']
    if not bm:
        return bm_ph.message_container('Bookmarks', 'Bookmarks list Empty')

    oc = ObjectContainer(title2='My Bookmarks', art=R(ART_PH), no_cache=True)

    for key in sorted(bm.keys()):
        if len(bm[key]) == 0:
            del Dict['Bookmarks'][key]
            Dict.Save()
        else:
            if key == 'PicPornstar':
                oc.add(DirectoryObject(
                    key=Callback(PicBookmarksSub, category=key),
                    title='Pornstars', summary='Display Pornstar Bookmarks',
                    thumb=R(ICON_PSTARS_PH), art=R(ART_PH)
                    ))
            elif key == 'PhotoAlbum':
                oc.add(DirectoryObject(
                    key=Callback(PicBookmarksSub, category=key),
                    title='Photo Albums', summary='Display Photo Albums Bookmarks',
                    thumb=R(ICON_PHOTOALBUM), art=R(ART_PH)
                    ))

    if len(oc) > 0:
        return oc
    else:
        return bm_ph.message_container('Bookmarks', 'Bookmark list Empty')

####################################################################################################
@route(PH_PREFIX + '/bookmarks/sub')
def PicBookmarksSub(category):
    """List Bookmarks Alphabetically"""

    bm = Dict['Bookmarks']
    if not category in bm.keys():
        return bm_ph.message_container('Error',
            '%s Bookmarks list is dirty, or no %s Bookmark list exist.' %(category, category))

    oc = ObjectContainer(title2='My Bookmarks | %s' %category, art=R(ART_PH), no_cache=True)

    for bookmark in sorted(bm[category], key=lambda k: k['title']):
        title = bookmark['title']
        thumb = bookmark['thumb']
        url = bookmark['url']
        category = bookmark['category']

        if category == 'PicPornstar':
            oc.add(DirectoryObject(
                key=Callback(PornstarPH, title=title, href=url, thumb=thumb),
                title=title, thumb=Resource.ContentsOfURLWithFallback(thumb, 'icon-babe-miss.png'),
                art=R(ART_PH)
                ))
        elif category == 'PhotoAlbum':
            oc.add(DirectoryObject(
                key=Callback(PhotoAlbumOpt, title=title, href=url, thumb=thumb),
                title=title, thumb=thumb, art=R(ART_PH)
                ))

    if len(oc) > 0:
        return oc
    else:
        return bm_ph.message_container('Bookmarks', '%s Bookmarks list Empty' %category)

####################################################################################################
@route(CH_PREFIX + '/directorylist', page=int)
def DirectoryList(title, href, page):
    """List Videos by page"""

    url = CH_BASE_URL + href

    html = HTML.ElementFromURL(url)

    nextpg_node = html.xpath('//li/a[@rel="next"]')
    if page == 1 and not nextpg_node:
        main_title = title
    else:
        main_title = '%s | Page %i' %(title, page) if nextpg_node else '%s | Page %i | Last Page' %(title, page)

    oc = ObjectContainer(title2=main_title, art=R(ART_CH))

    for node in html.xpath('//li[@itemtype]'):
        anode = node.xpath('./a[@class="t"]')[0]
        href = anode.get('href')
        vhref = CH_BASE_URL + href
        vid = href.split('/')[2]
        thumb = anode.xpath('./img/@src')[0].strip()

        dur_node = anode.xpath('./div[@class="tr"]/text()')[0].split(':')
        duration = (int(dur_node[0])*60000) + (int(dur_node[1])*1000)

        vtitle = node.xpath('./a[starts-with(@class, "vttl")]/text()')[0].strip()
        tagline = node.xpath('./div[starts-with(@class, "info")]/text()')[0].strip()

        video_info = {
            'id': vid,
            'title': vtitle,
            'duration': duration,
            'tagline': tagline,
            'thumb': thumb,
            'url': vhref
            }

        oc.add(DirectoryObject(
            key=Callback(VideoPage, video_info=video_info),
            title=vtitle, thumb=thumb, tagline=tagline, art=R(ART_CH)
            ))

    if nextpg_node:
        href = nextpg_node[0].get('href')
        if ('popular' in href) or ('pornstars' in href):
            nextpg = int(href.split('/')[4])
        else:
            nextpg = int(href.split('/')[3])
        oc.add(NextPageObject(
            key=Callback(DirectoryList, title=title, href=href, page=nextpg),
            title='Next Page>>', art=R(ART_CH)
            ))

    if len(oc) > 0:
        return oc
    else:
        return bm_ch.message_container('Video List', 'Video List Empty')

####################################################################################################
@route(PH_PREFIX + '/photoalbum/opt')
def PhotoAlbumOpt(title, thumb, href):
    """Setup Photo Album and bookmark options"""

    html = HTML.ElementFromURL(PH_BASE_URL + href)
    bm_id = href.split('/')[2]
    name = title.split('/')[-1].strip()
    match = bm_ch.bookmark_exist(item_id=bm_id, category='PhotoAlbum')
    photoalbum_exist = html.xpath('//meta[@name="description"]')
    header = None
    message = None

    if not photoalbum_exist and match:
        header = name
        message = 'This Photo Album is no longer available.'
    elif (not match) and (not photoalbum_exist):
        return bm_ph.message_container('Warning', 'This Photo Album is no longer available.')

    oc = ObjectContainer(title2=title, header=header, message=message, art=R(ART_PH), no_cache=True)

    if photoalbum_exist:
        oc.add(PhotoAlbumObject(
            key=Callback(PhotoBin, title=title, href=href),
            rating_key = PH_BASE_URL + href, source_title='PicHunter', title=name, thumb=thumb,
            art=R(ART_PH)
            ))
        oc.add(DirectoryObject(
            key=Callback(PhotoAlbumList, title='Related Galleries', href=href),
            title='Related Galleries', thumb=pichunter_list(html)[0][1], art=R(ART_PH)
            ))
        gstar = html.xpath('//a[@class="g_star r"]')
        if gstar:
            if len(gstar) == 1:
                gstar_href = gstar[0].get('href')
                gstar_title = gstar[0].text.strip()
                gstar_thumb = HTTP.Request(CH_BASE_URL + '/a/modelthumb?name=%s' %String.Quote(gstar_title, usePlus=True)).content
                oc.add(DirectoryObject(
                    key=Callback(PornstarPH, title=gstar_title, href=gstar_href, thumb=gstar_thumb),
                    title=gstar_title, thumb=gstar_thumb, art=R(ART_PH)
                    ))
            else:
                pstar_list = []
                for p in gstar:
                    gstar_href = p.get('href')
                    gstar_title = p.text.strip()
                    pstar_list.append((gstar_title, gstar_href))
                oc.add(DirectoryObject(
                    key=Callback(PornstarPHF, pstar_list=pstar_list),
                    title='Featured Pornstars', thumb=R(ICON_PSTARS_PH), art=R(ART_PH)
                    ))
        gsite = html.xpath('//a[@class="g_site"]')
        if gsite:
            gsite_href = gsite[0].get('href')
            gsite_title = gsite[0].text.strip()
            oc.add(DirectoryObject(
                key=Callback(Studio, title=gsite_title, href=gsite_href),
                title=gsite_title, thumb=R(ICON_STUDIO), art=R(ART_PH)
                ))

    bm_ph.add_remove_bookmark(
        oc=oc, title=name, thumb=thumb, url=href, item_id=bm_id,
        category='PhotoAlbum', duration=None, tagline=None
        )
    return oc

####################################################################################################
@route(PH_PREFIX + '/pornstar/featured', pstar_list=list)
def PornstarPHF(pstar_list):
    oc = ObjectContainer(title2='Featured Pornstars', art=R(ART_PH))
    for n, h in pstar_list:
        thumb = HTTP.Request(CH_BASE_URL + '/a/modelthumb?name=%s' %String.Quote(n, usePlus=True)).content
        oc.add(DirectoryObject(
            key=Callback(PornstarPH, title=n, href=h, thumb=thumb),
            title=n, thumb=thumb, art=R(ART_PH)
            ))
    return oc

####################################################################################################
@route(PH_PREFIX + '/photo/bin')
def PhotoBin(title, href):
    """Create PhotoAlbum for photos in href"""

    oc = ObjectContainer(title2=title, art=R(ART_PH))
    html = HTML.ElementFromURL(PH_BASE_URL + href)
    for node in html.xpath('//figure[@itemtype]/a'):
        name = node.get('title')
        thumb = node.get('href')
        oc.add(CreatePhotoObject(title=name, url=thumb))
    return oc

####################################################################################################
@route(CH_PREFIX + '/video/thumbs/bin')
def CHPhotoBin(title, thumb, url):
    """Create PhotoAlbum for photos in href"""

    oc = ObjectContainer(title2=title, art=R(ART_CH))
    page = HTTP.Request(url).content
    re_count = Regex(r'var\ mov\_thumbs\ \=\ (\d+?)\;').search(page)
    count = int(re_count.group(1)) if re_count else 30
    it = Regex(r'(.*)\_(\d+)(.*)').search(thumb)
    for i in xrange(count):
        oc.add(CreatePhotoObject(title=str(i+1), url=it.group(1)+'_%i' %(i+1)+it.group(3)))
    return oc

####################################################################################################
@route(CH_PREFIX + '/videopage', video_info=dict)
def VideoPage(video_info):
    """
    Video Sub Page
    Includes Similar Videos and Bookmark Option
    """

    html = HTML.ElementFromURL(video_info['url'])
    video_removed = html.xpath('//blockquote')
    match = bm_ch.bookmark_exist(item_id=video_info['id'], category='Video')
    header = None
    message = None

    if video_removed:
        if match:
            header = video_info['title']
            message = video_removed[0].text_content().strip()
        else:
            return bm_ch.message_container('Warning', 'This video is no longer available.')

    oc = ObjectContainer(title2=video_info['title'], header=header, message=message, art=R(ART_CH), no_cache=True)

    if not video_removed:
        oc.add(VideoClipObject(
            title=video_info['title'],
            duration=video_info['duration'],
            summary=video_info['tagline'],
            thumb=video_info['thumb'],
            art=R(ART_CH),
            url=video_info['url']
            ))

        oc.add(PhotoAlbumObject(
            key=Callback(CHPhotoBin, title=video_info['title'], thumb=video_info['thumb'], url=video_info['url']),
            rating_key = video_info['url']+'/thumbs', source_title='ClipHunter',
            title='Video Thumbs', thumb=R(ICON_PHOTOALBUM), art=R(ART_CH)
            ))

        related_thumb = html.xpath('//li[@itemtype]/a[@class="t"]/img/@src')[0]
        oc.add(DirectoryObject(
            key=Callback(DirectoryList, title='Related', href=video_info['url'].split(CH_BASE_URL)[1], page=1),
            title='Related Videos', thumb=related_thumb, art=R(ART_CH)
            ))
        mdl = html.xpath('//a[@class="materialButton mdl ps-popover"]')
        if mdl:
            p_name = mdl[0].text_content().strip()
            p_href = mdl[0].get('href').rsplit('/', 1)[0].replace(' ', '+')
            p_img = HTTP.Request(CH_BASE_URL + '/a/modelthumb?name=%s' %String.Quote(p_name, usePlus=True)).content
            oc.add(DirectoryObject(
                key=Callback(PornstarCH, title=p_name, href=p_href, thumb=p_img),
                title=p_name, thumb=p_img, art=R(ART_CH)
                ))
        chnl = html.xpath('//a[@class="materialButton chnl"]')
        if chnl:
            chnl_title = chnl[0].text_content().strip()
            chnl_href = chnl[0].get('href').replace(' ', '+')
            oc.add(DirectoryObject(
                key=Callback(HDOpt, title='Channels / '+chnl_title, href=chnl_href),
                title=chnl_title, thumb=R(ICON_TV), art=R(ART_CH)
                ))

    bm_ch.add_remove_bookmark(
        oc=oc, title=video_info['title'], thumb=video_info['thumb'], url=video_info['url'],
        item_id=video_info['id'], category='Video', duration=video_info['duration'],
        tagline=video_info['tagline']
        )

    return oc

####################################################################################################
@route(PH_PREFIX + '/create/photo/object', include_container=bool)
def CreatePhotoObject(title, url, include_container=False, *args, **kwargs):
    """create photo object for pichunter"""

    photo_object = PhotoObject(
        key=Callback(CreatePhotoObject, title=title, url=url, include_container=True),
            rating_key=url,
            source_title='PicHunter',
            title=title,
            thumb=url,
            art=R(ART_PH),
            items=[MediaObject(parts=[PartObject(key=url)])]
            )
    if include_container:
        return ObjectContainer(objects=[photo_object])
    else:
        return photo_object

####################################################################################################
def abc():
    return map(chr, range(ord('A'), ord('Z')+1))

####################################################################################################
def pichunter_list(html, relative=False):
    palist = []
    for node in html.xpath('%s//a[@class="thumb"]' %('.' if relative else '')):
        href = node.get('href')
        title = node.xpath('./img/@alt')[0]
        thumb = node.xpath('./img/@src')[0]
        palist.append((title, thumb, href))
    return palist

####################################################################################################
def nextpg_href(html):
    nextpg_node = html.xpath('//li/a[@rel="next"]')
    href = None
    if nextpg_node:
        href = nextpg_node[0].get('href')
    return href
