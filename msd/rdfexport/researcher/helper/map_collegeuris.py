#!/usr/bin/env python


def lookupCollege (college):
    
    lookup_table= [{'url':'http://www.all-souls.ox.ac.uk','college':'All Souls College',},
                    {'url':' http://www.balliol.ox.ac.uk','college':'Balliol College',},
                    {'url':' http://www.bfriars.ox.ac.uk','college':'Blackfriars',},
                    {'url':' http://www.bnc.ox.ac.uk','college':'Brasenose College ',},
                    {'url':' http://www.campion.ox.ac.uk','college':'Campion Hall',},
                    {'url':' http://www.chch.ox.ac.uk','college':'Christ Church',},
                    {'url':' http://www.ccc.ox.ac.uk','college':'Corpus Christi College',},
                    {'url':' http://www.exeter.ox.ac.uk','college':'Exeter College',},
                    {'url':' http://www.gtc.ox.ac.uk','college':'Green Templeton College',},
                    {'url':' http://www.hmc.ox.ac.uk','college':'Harris Manchester College',},
                    {'url':' http://www.hertford.ox.ac.uk','college':'Hertford College',},
                    {'url':' http://www.jesus.ox.ac.uk','college':'Jesus College',},
                    {'url':' http://www.keble.ox.ac.uk','college':'Keble College',},
                    {'url':' http://www.kellogg.ox.ac.uk','college':'Kellogg College',},
                    {'url':' http://www.lmh.ox.ac.uk','college':'Lady Margaret Hall',},
                    {'url':' http://www.linacre.ox.ac.uk','college':'Linacre College',},
                    {'url':' http://www.lincoln.ox.ac.uk','college':'Lincoln College',},
                    {'url':' http://www.magd.ox.ac.uk','college':'Magdalen College',},
                    {'url':' http://www.mansfield.ox.ac.uk','college':'Mansfield College',},
                    {'url':' http://www.merton.ox.ac.uk','college':'Merton College',},
                    {'url':' http://www.new.ox.ac.uk','college':'New College',},
                    {'url':' http://www.nuffield.ox.ac.uk','college':'Nuffield College ',},
                    {'url':' http://www.oriel.ox.ac.uk','college':'Oriel College ',},
                    {'url':' http://www.pmb.ox.ac.uk','college':'Pembroke College ',},
                    {'url':' http://www.rpc.ox.ac.uk','college':'Regent\'s Park College',},
                    {'url':' http://www.some.ox.ac.uk','college':'Somerville College',},
                    {'url':' http://www.st-annes.ox.ac.uk','college':'St Anne\'s College',},
                    {'url':' http://www.sant.ox.ac.uk','college':'St Antony\'s College',},
                    {'url':' http://www.st-benets.ox.ac.uk','college':'St Benet\'s Hall',},
                    {'url':' http://www.stcatz.ox.ac.uk','college':'St Catherine\'s College',},
                    {'url':' http://www.stx.ox.ac.uk','college':'St Cross College',},
                    {'url':' http://www.seh.ox.ac.uk','college':'St Edmund Hall',},
                    {'url':' http://www.st-hildas.ox.ac.uk','college':'St Hilda\'s College',},
                    {'url':' http://www.st-hughs.ox.ac.uk','college':'St Hugh\'s College',},
                    {'url':' http://www.sjc.ox.ac.uk','college':'St John\'s College ',},
                    {'url':' http://www.spc.ox.ac.uk','college':'St Peter\'s College',},
                    {'url':' http://www.ssho.ox.ac.uk','college':'St Stephen\'s House',},
                    {'url':' http://www.queens.ox.ac.uk','college':'The Queen\'s College',},
                    {'url':' http://www.trinity.ox.ac.uk','college':'Trinity College',},
                    {'url':' http://www.univ.ox.ac.uk','college':'University College',},
                    {'url':' http://www.wadham.ox.ac.uk','college':'Wadham College',},
                    {'url':' http://www.wolfson.ox.ac.uk','college':'Wolfson College',},
                    {'url':' http://www.worc.ox.ac.uk','college':'Worcester College',},
                    {'url':' http://www.wycliffe.ox.ac.uk','college':'Wycliffe Hall',},
                    ]
                    
    for x in lookup_table:
        if x['college'] == college:
            return x['url']
            
    return 'nourl'