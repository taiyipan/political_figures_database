import sqlite3
import json

# create database
dbname = 'political_figures_database.sqlite'
conn = sqlite3.connect(dbname)
cur = conn.cursor()

# make tables
cur.executescript('''
    DROP TABLE IF EXISTS house_members;
    DROP TABLE IF EXISTS senate_members;

    CREATE TABLE IF NOT EXISTS house_members (
        id                           VARCHAR(15)    PRIMARY KEY,
        title                        VARCHAR(20),
        short_title                  VARCHAR(10),
        api_uri                      VARCHAR(50),
        first_name                   VARCHAR(25)    NOT NULL,
        middle_name                  VARCHAR(25),
        last_name                    VARCHAR(25)    NOT NULL,
        suffix                       VARCHAR(10),
        date_of_birth                DATE,
        gender                       CHAR(1),
        party                        CHAR(1),
        leadership_role              VARCHAR(50),
        twitter_account              VARCHAR(30),
        facebook_account             VARCHAR(30),
        youtube_account              VARCHAR(30),
        govtrack_id                  INT,
        cspan_id                     INT,
        votesmart_id                 INT,
        icpsr_id                     INT,
        crp_id                       VARCHAR(40),
        google_entity_id             VARCHAR(40),
        fec_candidate_id             VARCHAR(40),
        url                          VARCHAR(50),
        rss_url                      VARCHAR(50),
        contact_form                 VARCHAR(50),
        in_office                    BIT,
        cook_pvi                     VARCHAR(10),
        dw_nominate                  DECIMAL(10, 3),
        ideal_point                  VARCHAR(20),
        seniority                    INT,
        next_election                YEAR,
        total_votes                  INT,
        missed_votes                 INT,
        total_present                INT,
        last_updated                 DATETIME,
        ocd_id                       VARCHAR(50),
        office                       VARCHAR(50),
        phone                        VARCHAR(20),
        fax                          VARCHAR(20),
        state                        CHAR(2),
        district                     VARCHAR(10),
        at_large                     BIT,
        geoid                        INT,
        missed_votes_pct             DECIMAL(5, 2),
        votes_with_party_pct         DECIMAL(5, 2),
        votes_against_party_pct      DECIMAL(5, 2)
    );

    CREATE TABLE IF NOT EXISTS senate_members (
        id                           VARCHAR(15)    PRIMARY KEY,
        title                        VARCHAR(20),
        short_title                  VARCHAR(10),
        api_uri                      VARCHAR(50),
        first_name                   VARCHAR(25)    NOT NULL,
        middle_name                  VARCHAR(25),
        last_name                    VARCHAR(25)    NOT NULL,
        suffix                       VARCHAR(10),
        date_of_birth                DATE,
        gender                       CHAR(1),
        party                        CHAR(1),
        leadership_role              VARCHAR(50),
        twitter_account              VARCHAR(30),
        facebook_account             VARCHAR(30),
        youtube_account              VARCHAR(30),
        govtrack_id                  INT,
        cspan_id                     INT,
        votesmart_id                 INT,
        icpsr_id                     INT,
        crp_id                       VARCHAR(40),
        google_entity_id             VARCHAR(40),
        fec_candidate_id             VARCHAR(40),
        url                          VARCHAR(50),
        rss_url                      VARCHAR(50),
        contact_form                 VARCHAR(50),
        in_office                    BIT,
        cook_pvi                     VARCHAR(10),
        dw_nominate                  DECIMAL(10, 3),
        ideal_point                  VARCHAR(20),
        seniority                    INT,
        next_election                YEAR,
        total_votes                  INT,
        missed_votes                 INT,
        total_present                INT,
        last_updated                 DATETIME,
        ocd_id                       VARCHAR(50),
        office                       VARCHAR(50),
        phone                        VARCHAR(20),
        fax                          VARCHAR(20),
        state                        CHAR(2),
        senate_class                 INT,
        state_rank                   VARCHAR(10),
        lis_id                       VARCHAR(10),
        missed_votes_pct             DECIMAL(5, 2),
        votes_with_party_pct         DECIMAL(5, 2),
        votes_against_party_pct      DECIMAL(5, 2)
    );
''')

# data source
house_members_fname = 'members_116/116_house_members.json'
senate_members_fname = 'members_116/116_senate_members.json'

# open files and read as JSON data
house_members = json.loads(open(house_members_fname).read())
senate_members = json.loads(open(senate_members_fname).read())

# read and insert data insert into house_members tables
cycle = 0
for entry in house_members['results'][0]['members']:
    try:
        cur.execute('''
            INSERT OR IGNORE INTO house_members (
                id,
                title,
                short_title,
                api_uri,
                first_name,
                middle_name,
                last_name,
                suffix,
                date_of_birth,
                gender,
                party,
                leadership_role,
                twitter_account,
                facebook_account,
                youtube_account,
                govtrack_id,
                cspan_id,
                votesmart_id,
                icpsr_id,
                crp_id,
                google_entity_id,
                fec_candidate_id,
                url,
                rss_url,
                contact_form,
                in_office,
                cook_pvi,
                dw_nominate,
                ideal_point,
                seniority,
                next_election,
                total_votes,
                missed_votes,
                total_present,
                last_updated,
                ocd_id,
                office,
                phone,
                fax,
                state,
                district,
                at_large,
                geoid,
                missed_votes_pct,
                votes_with_party_pct,
                votes_against_party_pct
            )
            VALUES (
                ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,
                ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,
                ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,
                ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,
                ?, ?, ?, ?, ?, ?
            )
        ''', (
            entry['id'],
            entry['title'],
            entry['short_title'],
            entry['api_uri'],
            entry['first_name'],
            entry['middle_name'],
            entry['last_name'],
            entry['suffix'],
            entry['date_of_birth'],
            entry['gender'],
            entry['party'],
            entry['leadership_role'],
            entry['twitter_account'],
            entry['facebook_account'],
            entry['youtube_account'],
            entry['govtrack_id'],
            entry['cspan_id'],
            entry['votesmart_id'],
            entry['icpsr_id'],
            entry['crp_id'],
            entry['google_entity_id'],
            entry['fec_candidate_id'],
            entry['url'],
            entry['rss_url'],
            entry['contact_form'],
            entry['in_office'],
            entry['cook_pvi'],
            entry['dw_nominate'],
            entry['ideal_point'],
            entry['seniority'],
            entry['next_election'],
            entry['total_votes'],
            entry['missed_votes'],
            entry['total_present'],
            entry['last_updated'],
            entry['ocd_id'],
            entry['office'],
            entry['phone'],
            entry['fax'],
            entry['state'],
            entry['district'],
            entry['at_large'],
            entry['geoid'],
            entry['missed_votes_pct'],
            entry['votes_with_party_pct'],
            entry['votes_against_party_pct']
        ))
        # update cycle
        cycle += 1
        # commit
        if cycle % 10 == 0:
            conn.commit()
    except:
        print(entry)
# final commit
conn.commit()

# read and insert data insert into senate_members tables
cycle = 0
for entry in senate_members['results'][0]['members']:
    try:
        cur.execute('''
            INSERT OR IGNORE INTO senate_members (
                id,
                title,
                short_title,
                api_uri,
                first_name,
                middle_name,
                last_name,
                suffix,
                date_of_birth,
                gender,
                party,
                leadership_role,
                twitter_account,
                facebook_account,
                youtube_account,
                govtrack_id,
                cspan_id,
                votesmart_id,
                icpsr_id,
                crp_id,
                google_entity_id,
                fec_candidate_id,
                url,
                rss_url,
                contact_form,
                in_office,
                cook_pvi,
                dw_nominate,
                ideal_point,
                seniority,
                next_election,
                total_votes,
                missed_votes,
                total_present,
                last_updated,
                ocd_id,
                office,
                phone,
                fax,
                state,
                senate_class,
                state_rank,
                lis_id,
                missed_votes_pct,
                votes_with_party_pct,
                votes_against_party_pct
            )
            VALUES (
                ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,
                ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,
                ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,
                ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,
                ?, ?, ?, ?, ?, ?
            )
        ''', (
            entry['id'],
            entry['title'],
            entry['short_title'],
            entry['api_uri'],
            entry['first_name'],
            entry['middle_name'],
            entry['last_name'],
            entry['suffix'],
            entry['date_of_birth'],
            entry['gender'],
            entry['party'],
            entry['leadership_role'],
            entry['twitter_account'],
            entry['facebook_account'],
            entry['youtube_account'],
            entry['govtrack_id'],
            entry['cspan_id'],
            entry['votesmart_id'],
            entry['icpsr_id'],
            entry['crp_id'],
            entry['google_entity_id'],
            entry['fec_candidate_id'],
            entry['url'],
            entry['rss_url'],
            entry['contact_form'],
            entry['in_office'],
            entry['cook_pvi'],
            entry['dw_nominate'],
            entry['ideal_point'],
            entry['seniority'],
            entry['next_election'],
            entry['total_votes'],
            entry['missed_votes'],
            entry['total_present'],
            entry['last_updated'],
            entry['ocd_id'],
            entry['office'],
            entry['phone'],
            entry['fax'],
            entry['state'],
            entry['senate_class'],
            entry['state_rank'],
            entry['lis_id'],
            entry['missed_votes_pct'],
            entry['votes_with_party_pct'],
            entry['votes_against_party_pct']
        ))
        # update cycle
        cycle += 1
        # commit
        if cycle % 10 == 0:
            conn.commit()
    except:
        print(entry)
# final commit
conn.commit()
