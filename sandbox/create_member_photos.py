from django.core.files import File
from charterclub.models import *

# Insert Members
member_list = [("Jean-Carlos", "Arenas", "jarenas", 2016),
("Rory", "Fitzpatrick", "roryf", 2016),
("Robert", "DeNunzio", "rad3", 2016),
("Daniel", "Dore", "ddore", 2016),
("Megan", "Abbott", "msabbott", 2016),
("Cynthia", "Tremonte", "cat3", 2016),
("Kelsey", "Blair", "kblair", 2016),
("Eric", "Blum", "ecblum", 2016),
("Mo", "Luo", "moluo", 2016),
("Shirley", "Zhu", "shirleyz", 2016),
("Hannah", "Miller", "hannahgm", 2016),
("Dennis", "Smith", "dennisds", 2016),
("Daniel", "Zirkel", "dzirkel", 2016),
("Dorothy", "Chen", "dschen", 2016),
("Liam", "Kelly", "ljkelly", 2016),
("Eric", "Principato", "erictp", 2016),
("Curtis", "Belmonte", "curtislb", 2016),
("Yuriko", "Inaba", "yinaba", 2016),
("Jeremy", "Whitton", "jwhitton", 2016),
("Gabriel", "Ambruso", "gambruso", 2015),
("Proma", "Banerjee", "pbanerje", 2015),
("Gabriel", "Baraban", "gbaraban", 2015),
("Valentina", "Barboy", "vbarboy", 2015),
("Lauren", "Berdick", "lberdick", 2015),
("Alison", "Bick", "bick", 2015),
("Emily", "Bobrick", "ebobrick", 2015),
("Daniel", "Brooker", "dbrooker", 2015),
("Jeffrey", "Cady", "cady", 2015),
("Regina", "Cai", "rrcai", 2015),
("Harrison", "Cape", "hcape", 2015),
("Anna", "Cardinal", "cardinal", 2015),
("Amanda", "Chen", "aachen", 2015),
("Jonathan", "Chen", "jc33", 2015),
("Shompa", "Choudhury", "schoudhu", 2015),
("Stephen  Y.", "Cognetta", "cognetta", 2015),
("Cara", "de Freitas Bart", "cnde", 2015,),
("Karthik", "Dhore", "kdhore", 2015),
("David", "Durst", "ddurst", 2015),
("David", "Dyrda", "ddyra", 2015),
("Glenn", "Fisher", "gfisher", 2015),
("Mary", "Gilstad", "mgilstad", 2015),
("Emma", "Glennon", "eglennon", 2015),
("Damir", "Golac", "dgolac", 2015),
("Amy", "Gonzalez", "akgonzal", 2015),
("Neil", "Hannan", "nhannan", 2015),
("Jessica", "Hao", "hao", 2015),
("David", "Harris", "hgdavis", 2015),
("Stephanie", "He", "syhe", 2015),
("Thomas", "Horton", "thorton", 2015),
("Tianyuan", "Huang", "tianyuan", 2015),
("Bryan", "Jacobowitz", "bjacobow", 2015),
("Andrew", "Jeon", "ajeon", 2015),
("Daniel", "Johnson", "dpjohnso", 2015),
("Silken", "Jones", "smjones", 2015),
("Megan", "Kennedy", "mkthree", 2015),
("Elijah", "Kolmes", "ekolmes", 2015),
("Benjamin", "Koons", "bkoons", 2015),
("Daria", "Koren", "dkoren", 2015),
("Gregory", "Kraft", "gkraft", 2015),
("Alisa", "Kroutikova", "akroutik", 2015),
("Aaron C.", "Ladd", "aladd", 2015),
("Harrison", "Lee", "htlee", 2015),
("Jessica", "Liang", "jsliang", 2015),
("Kevin", "Liaw", "kliaw", 2015),
("Beau", "Lovdahl", "blovdahl", 2015),
("Nicholas", "Mai", "nmai", 2015),
("Ryan", "McNellis", "mcnellis", 2015),
("Jack", "Moore", "jcmtwo", 2015),
("Lauren", "Morera", "lmorera", 2015),
("Rachel", "Myers", "rmyers", 2015),
("Buyan", "Pan", "bpan", 2015),
("Charles", "Peyser", "peyser", 2015),
("Erica", "Portnoy", "eportnoy", 2015),
("Graham", "Read", "gread", 2015),
("Francis", "Ricci", "fjricci", 2015),
("Nicholas", "Robinson", "ncrobins", 2015),
("Ruth", "Rosenthal", "rbrosent", 2015),
("Shubhro", "Saha", "saha", 2015),
("Matthew", "Shackelford", "mvshacke", 2015),
("Eric ", "Shullman", "shullman", 2015),
("Alexander", "Smith", "adsmith", 2015),
("Adam", "Smyles", "asymles", 2015),
("Kai", "Song-Nichols", "kasong", 2015),
("Benjamin", "Tien", "btien", 2015),
("Joseph", "Turchiano", "jturchia", 2015),
("Matthew", "Walsh", "mtwalsh", 2015),
("Austin", "Wang", "austinw", 2015),
("Yolanda Y", "Yeh", "yoyeh", 2015),
("Quan", "Zhou", "quanzhou", 2015),
("Joshua", "Zimmer", "jazimmer", 2015),
("Brian", "Kernigan", "bwk", 2015),
("Amy", "Tai", "amytai", 2015),
("Christopher", "Moretti", "cmoretti", 2015),
("X. Kelvin", "Zou", "xuanz", 2015),
("Elba", "Garza", "elba", 2015),
("Tom", "Wu", "tongbinw", 2015)]


member_list = member_list + \
    [('Jean-Carlos','Arenas','jarenas', 2016, 255.00),
    ('Andra','Bailard','abailard', 2016, 225.00),
    ('Curtis','Belmonte','curtislb', 2016, 255.00),
    ('Kelsey','Blair','kblair', 2016, 255.00),
    ('Eric','Blum','ecblum', 2016, 255.00),
    ('Cara','Cavanaugh','carapc', 2016, 225.00),
    ('Paul','Chang','pc9', 2016, 225.00),
    ('Jeremy','Cheehan','jcheehan', 2016, 225.00),
    ('Dorothy','Chen','dschen', 2016, 255.00),
    ('Carol','Chiu','cwchiu', 2016, 255.00),
    ('David','Cruikshank','dac3', 2016, 255.00),
    ('Anirudh','Dasarathy','anirudhd', 2016, 225.00),
    ('Robert', 'Denunzio','rad3', 2016, 190.00),
    ('Daniel','Dore','ddore', 2016, 255.00),
    ('Riley','Fitzgerald','rileyf', 2016, 225.00),
    ('Rory','Fitzpatrick','roryf', 2016, 255.00),
    ('Damini','Ghosh','dghosh', 2016, 225.00),
    ('Kristin','Goehl','kgoehl', 2016, 225.00),
    ('Natalie','Hejduk','nhejduk', 2016, 225.00),
    ('Yuriko','Inaba','yinaba', 2016, 255.00),
    ('Angeline','Jacques','ajacques', 2016, 225.00),
    ('Ghassen','Jerfel','gjerfel', 2016, 225.00),
    ('Max','Kaplan','kaplanm', 2016, 225.00),
    ('Liam','Kelly','ljkelly', 2016, 255.00),
    ('Ilya','Krasnovsky','ilyak', 2016, 225.00),
    ('Kenny','Lin','kennylin', 2016, 225.00),
    ('Kathryn','Long','kclong', 2016, 225.00),
    ('Mo','Luo','moluo', 2016, 255.00),
    ('Saahil','Madge','smadge', 2016, 225.00),
    ('Eve','Matthaey','matthaey', 2016, 225.00),
    ('Lucas','Mayer','ljmayer', 2016, 225.00),
    ('Nicholas Afee','nmcafee', 2016, 225.00),
    ('Hannah','Miller','hannahgm', 2016, 255.00),
    ('Alexander','Payne','ajpayne', 2016, 225.00),
    ('Richard','Polo','rpolo', 2016, 225.00),
    ('Eric','Principato','erictp', 2016, 255.00),
    ('Hansen','Qian','hq', 2016, 225.00),
    ('Alec Jacob','Ranzato','aranzato', 2016, 225.00),
    ('Brent','Read','bread', 2016, 225.00),
    ('Jack','Reed','jnreed', 2016, 225.00),
    ('Christian','Rodriguez','cer3', 2016, 225.00),
    ('Abdiel','Santiago','abdiels', 2016, 225.00),
    ('Karthik','Sastry','ksastry', 2016, 225.00),
    ('Joseph','Scherrer','jrs3', 2016, 225.00),
    ('Zachary','Schiffer','zjs', 2016, 225.00),
    ('Kevin','Silmore','kss', 2016, 225.00),
    ('Matthew','Silver','mssilver', 2016, 225.00),
    ('Dennis','Smith','dennisds', 2016, 255.00),
    ('Sofia','Suarez','sesuarez', 2016, 225.00),
    ('Leann','Thayaparan','lpgt', 2016, 225.00),
    ('Cynthia','Tremonte','cat3', 2016, 255.00),
    ('Erica','Tsai','eytsai', 2016, 225.00),
    ('Mariel Va','Landingham','mlv', 2016, 225.00),
    ('Michael','Wang','mjwang', 2016, 225.00),
    ('Jeremy','Whitton','jwhitton', 2016, 255.00),
    ('Sally','Yu','swyu', 2016, 225.00),
    ('Christopher','Yuk','cyuk', 2016, 225.00),
    ('Irvin','Zhan','izhan', 2016, 225.00),
    ('Kevin','Zhang','krzhang', 2016, 225.00),
    ('Shirley','Zhu','shirleyz', 2016, 255.00),
    ('Daniel','Zirkel','dzirkel', 2016, 255.00),
    ('Joshua','Zuckerman','jrz', 2016, 255.00)]
# Insert member images - NOTE. MUST HAVE THE MEMBER IMAGES SAVED IN '/media/member_images/<netid>'
# you ALSO need to be the project root directory
for row in member_list:
    try:
        netid = row[2]
        url = 'media/member_images/%s.jpg' % netid
        image = File(open(url))

        m_o = Member.objects.filter(netid=netid)[0]
        m_o.image.save(url, image)
        m_o.save()
    except:
        print "Could not find an image for member: %s %s" % (row[0], row[1])