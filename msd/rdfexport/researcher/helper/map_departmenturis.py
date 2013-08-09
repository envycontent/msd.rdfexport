#!/usr/bin/env python


    
    #this and the function below are a horrible hack for the moment....
    
lookup_table= [{'dept':'Department of Psychiatry','url':'http://www.psychiatry.ox.ac.uk'},
                    {'dept':'Department of Experimental Psychology','url':'http://www.psy.ox.ac.uk'},
                    {'dept':'Department of Ophthalmology','url':'http://www.eye.ox.ac.uk'},
                    {'dept':'Experimental Psychology','url':'http://www.psy.ox.ac.uk'},
                    {'dept':'Department of Physiology, Anatomy and Genetics','url':'http://www.dpag.ox.ac.uk'},
                    {'dept':'Nuffield Department of Anaesthetics','url':'http://www.nda.ox.ac.uk'},
                    {'dept':'Nuffield Department of Surgery','url':'http://www.surgery.ox.ac.uk'},
                    {'dept':'Department of Clinical Pharmacology','url':'http://www.clinpharm.ox.ac.uk'},
                    {'dept':'Department of Paediatrics','url':'http://www.paediatrics.ox.ac.uk'},
                    {'dept':'Nuffield Department of Clinical Medicine','url':'http://www.ndm.ox.ac.uk'},
                    {'dept':'Department of Pharmacology','url':'http://www.pharm.ox.ac.uk'},
                    {'dept':'Sir William Dunn School of Pathology','url':'http://www.path.ox.ac.uk'},
                    {'dept':'Department of Cardiovascular Medicine','url':'http://www.cardiov.ox.ac.uk'},
                    {'dept':'Division of Public Health & Primary Health Care','url':'http://www.dphpc.ox.ac.uk'},
                    {'dept':'Nuffield Department of Clinical Laboratory Sciences','url':'http://www.ndcls.ox.ac.uk'},
                    {'dept':'Department of Clinical Neurology','url':'http://www.clneuro.ox.ac.uk'},
                    {'dept':'Department of Medical Oncology','url':'http://www.medonc.ox.ac.uk'},
                    {'dept':'Department of Oncology', 'url':'http://www.oncology.ox.ac.uk'},
                    {'dept':'Nuffield Department of Clinical Neurosciences', 'url':'http://www.ndcn.ox.ac.uk'},
                    {'dept':'Nuffield Department of Orthopaedic Surgery','url':'http://www.ndorm.ox.ac.uk'},
                    {'dept':'Nuffield Department of Orthopaedics, Rheumatology and Musculoskeletal Sciences','url':'http://www.ndorm.ox.ac.uk'},
                    {'dept':'Department of Biochemistry','url':'http://www.bioch.ox.ac.uk'},
                    {'dept':'Nuffield Department of Obstetrics and Gynaecology','url':'http://www.obs-gyn.ox.ac.uk'},
                    {'dept':'Medical Sciences','url':'http://www.medsci.ox.ac.uk'},
                    {'dept':'Wellcome Trust Centre for Human Genetics','url':'http://www.well.ox.ac.uk'},
                    {'dept':'Oxford Centre for Functional Magnetic Resonance Imaging of the Brain','url':'http://www.fmrib.ox.ac.uk'},
                    {'dept':'Weatherall Institute of Molecular Medicine','url':'http://www.imm.ox.ac.uk'},
                    {'dept':'BHF Molecular Cardiology Laboratory','url':''},
                    {'dept':'Department of Public Health','url':'http://www.dph.ox.ac.uk/'},
                    {'dept':'Department of Radiation Oncology & Biology','url':'http://www.rob.ox.ac.uk'},
                    {'dept':'Department of Primary Care Health Sciences','url':'http://www.phc.ox.ac.uk'},
                    {'dept':'Clinical Trial Service Unit & Epidemiological Studies Unit','url':'http://www.ctsu.ox.ac.uk'},
                    {'dept':'Oxford Centre for Diabetes, Endocrinology and Metabolism','url':'http://www.ocdem.ox.ac.uk'},
                    {'dept':'Nuffield Department of Clinical Medicine - JR Division','url':'http://www.ndm.ox.ac.uk/jr/'},
                    {'dept':'Localhost','url':'http://localhost:8080'},
                    ]

def lookupDept(url):
    for x in lookup_table:
        if x['url'] == url:
            return True           
    return False

def lookupURL(dept):                   
    for x in lookup_table:
        if x['dept'] == dept:
            return x['url']
            
    return ''