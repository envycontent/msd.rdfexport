import re
import urlparse
from BeautifulSoup import BeautifulSoup, SoupStrainer

from zope import interface
from zope import component
import Acquisition


from Products.CMFPlone.interfaces import IPloneSiteRoot



def fix_urls(text, absolute_url):
    anchor_exp = re.compile('#\w+')
    root_exp = re.compile('^/')
    relative_exp = re.compile('^(?!(\w+://|mailto:|javascript:|/))')
    soup = BeautifulSoup(text, fromEncoding='UTF-8') # hmm
    curl = absolute_url
    curl_parts = curl.split('/')
    
    url = absolute_url[1]
    if url.endswith('/'):
        site_url = url[:-1]
    else: 
        site_url = url

    if absolute_url.endswith('/'):
        context_url = absolute_url[:-1]
    else:
        context_url = absolute_url
    
    for attr in ('href', 'src'):                
        for tag in soup.findAll(SoupStrainer(**{attr:root_exp})):
            if len(curl_parts) > 3 and \
                   ':' in curl_parts[2] and \
                   tag[attr].startswith('/%s/' % curl_parts[3]):
                tag[attr] = '/'+'/'.join(tag[attr].split('/')[2:])

            # Kupu makes absolute links without the domain, which
            # include the Plone site, so let's try and strip the
            # Plone site's id out:
            site_id = component.getUtility(IPloneSiteRoot).getId()
            if tag[attr].startswith('/%s/' % site_id):
                tag[attr] = tag[attr].replace('/%s/' % site_id, '/', 1)

            tag[attr] = '%s%s' % (site_url, tag[attr])

        for tag in soup.findAll(SoupStrainer(**{attr:relative_exp})):
            if tag[attr].startswith('#'):
                tag[attr] = context_url + tag[attr]
                continue
            
            parts = (context_url + '/'+ tag[attr]).split('/')
            while '..' in parts:
                dots = parts.index('..')
                del parts[dots-1:dots+1]
            tag[attr] = '/'.join(parts)

        for tag in soup.findAll(SoupStrainer(**{attr:anchor_exp})):
            prot, dom, path, params, query, frag =  urlparse.urlparse(tag[attr])

            if not prot or not dom:
                tag[attr] = '#%s' % frag
                continue
            
            url = '%s://%s%s' % (prot, dom, path)
            if url.endswith('/'):
                url = url[:-1]

            # If the url points to our context and the anchor exists in our
            # text we change it to a bare anchor.
            # XXX: Maybe this should work with links to non-default views.
            if url == context_url:
                for match in soup.findAll(attrs=dict(name=frag)):
                    if match.name == u'a':
                        tag[attr] = '#%s' % frag                            

        
    return str(soup)
   