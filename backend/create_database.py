import sqlite3
import json

# create database
dbname = 'political_figures_database.db'
conn = sqlite3.connect(dbname)
cur = conn.cursor()

# make tables
cur.executescript('''
    DROP TABLE IF EXISTS house_members;
    DROP TABLE IF EXISTS senate_members;
    DROP TABLE IF EXISTS house_votes;
    DROP TABLE IF EXISTS senate_votes;
    DROP TABLE IF EXISTS house_voting_records;
    DROP TABLE IF EXISTS senate_voting_records;

    CREATE TABLE IF NOT EXISTS house_members (
        id                           VARCHAR(10)    PRIMARY KEY,
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
        id                           VARCHAR(10)    PRIMARY KEY,
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

    CREATE TABLE IF NOT EXISTS house_votes (
        id                                    INTEGER            PRIMARY KEY       AUTOINCREMENT,
        congress                              INT,
        session                               INT,
        chamber                               VARCHAR(10),
        roll_call                             INT,
        source                                VARCHAR(100),
        url                                   VARCHAR(100),
        bill_id                               VARCHAR(20),
        bill_number                           VARCHAR(20),
        bill_api_uri                          VARCHAR(100),
        bill_title                            VARCHAR(1000),
        bill_short_title                      VARCHAR(500),
        bill_latest_action                    VARCHAR(200),
        amendment_number                      VARCHAR(20),
        amendment_api_uri                     VARCHAR(100),
        amendment_sponsor_id                  VARCHAR(20),
        amendment_sponsor                     VARCHAR(50),
        amendment_sponsor_uri                 VARCHAR(100),
        amendment_sponsor_party               CHAR(1),
        amendment_sponsor_state               CHAR(2),
        question                              VARCHAR(200),
        question_text                         VARCHAR(200),
        description                           VARCHAR(500),
        vote_type                             VARCHAR(50),
        date                                  DATE,
        time                                  TIME,
        result                                VARCHAR(20),
        democratic_yes                        INT,
        democratic_no                         INT,
        democratic_present                    INT,
        democratic_not_voting                 INT,
        democratic_majority_position          VARCHAR(10),
        republican_yes                        INT,
        republican_no                         INT,
        republican_present                    INT,
        republican_not_voting                 INT,
        republican_majority_position          VARCHAR(10),
        independent_yes                       INT,
        independent_no                        INT,
        independent_present                   INT,
        independent_not_voting                INT,
        total_yes                             INT,
        total_no                              INT,
        total_present                         INT,
        total_not_voting                      INT
    );

    CREATE TABLE IF NOT EXISTS senate_votes (
        id                                    INTEGER            PRIMARY KEY       AUTOINCREMENT,
        congress                              INT,
        session                               INT,
        chamber                               VARCHAR(10),
        roll_call                             INT,
        source                                VARCHAR(100),
        url                                   VARCHAR(100),
        bill_id                               VARCHAR(20),
        bill_number                           VARCHAR(20),
        bill_api_uri                          VARCHAR(100),
        bill_title                            VARCHAR(1000),
        bill_short_title                      VARCHAR(500),
        bill_latest_action                    VARCHAR(200),
        amendment_number                      VARCHAR(20),
        amendment_api_uri                     VARCHAR(100),
        amendment_sponsor_id                  VARCHAR(20),
        amendment_sponsor                     VARCHAR(50),
        amendment_sponsor_uri                 VARCHAR(100),
        amendment_sponsor_party               CHAR(1),
        amendment_sponsor_state               CHAR(2),
        question                              VARCHAR(200),
        question_text                         VARCHAR(200),
        description                           VARCHAR(500),
        vote_type                             VARCHAR(50),
        date                                  DATE,
        time                                  TIME,
        result                                VARCHAR(20),
        tie_breaker                           VARCHAR(100),
        tie_breaker_vote                      VARCHAR(100),
        document_number                       VARCHAR(50),
        document_title                        VARCHAR(200),
        democratic_yes                        INT,
        democratic_no                         INT,
        democratic_present                    INT,
        democratic_not_voting                 INT,
        democratic_majority_position          VARCHAR(10),
        republican_yes                        INT,
        republican_no                         INT,
        republican_present                    INT,
        republican_not_voting                 INT,
        republican_majority_position          VARCHAR(10),
        independent_yes                       INT,
        independent_no                        INT,
        independent_present                   INT,
        independent_not_voting                INT,
        total_yes                             INT,
        total_no                              INT,
        total_present                         INT,
        total_not_voting                      INT
    );

    CREATE TABLE IF NOT EXISTS house_voting_records (
        id            INTEGER          PRIMARY KEY           AUTOINCREMENT,
        vote_id       INTEGER          REFERENCES house_votes (id),
        member_id     VARCHAR(10)      REFERENCES house_members (id),
        vote          VARCHAR(10)      DEFAULT NULL
    );

    CREATE TABLE IF NOT EXISTS senate_voting_records (
        id            INTEGER          PRIMARY KEY           AUTOINCREMENT,
        vote_id       INTEGER          REFERENCES senate_votes (id),
        member_id     VARCHAR(10)      REFERENCES senate_members (id),
        vote          VARCHAR(10)      DEFAULT NULL
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

# create votes tables
house_prefix = 'rollcall_votes/house_116/vote_'
senate_prefix = 'rollcall_votes/senate_116/vote_'
suffix = '.json'

# read and insert data into house_votes
cycle = 0
for i in range(1, 2000):
    try:
        fname = house_prefix + str(i) + suffix
        house_vote = json.loads(open(fname).read())
        print('Scanning', fname)
    except IOError:
        print('Source exhausted.')
        break
    v = house_vote['results']['votes']['vote']
    cur.execute('''
        INSERT INTO house_votes (
            congress,
            session,
            chamber,
            roll_call,
            source,
            url,
            bill_id,
            bill_number,
            bill_api_uri,
            bill_title,
            bill_short_title,
            bill_latest_action,
            amendment_number,
            amendment_api_uri,
            amendment_sponsor_id,
            amendment_sponsor,
            amendment_sponsor_uri,
            amendment_sponsor_party,
            amendment_sponsor_state,
            question,
            question_text,
            description,
            vote_type,
            date,
            time,
            result,
            democratic_yes,
            democratic_no,
            democratic_present,
            democratic_not_voting,
            democratic_majority_position,
            republican_yes,
            republican_no,
            republican_present,
            republican_not_voting,
            republican_majority_position,
            independent_yes,
            independent_no,
            independent_present,
            independent_not_voting,
            total_yes,
            total_no,
            total_present,
            total_not_voting
        ) VALUES (
            ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,
            ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,
            ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,
            ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,
            ?, ?, ?, ?
        )''', (
        v['congress'],
        v['session'],
        v['chamber'],
        v['roll_call'],
        v['source'],
        v['url'],
        v['bill'].get('bill_id'),
        v['bill'].get('number'),
        v['bill'].get('api_uri'),
        v['bill'].get('title'),
        v['bill'].get('short_title'),
        v['bill'].get('latest_action'),
        v['amendment'].get('number'),
        v['amendment'].get('api_uri'),
        v['amendment'].get('sponsor_id'),
        v['amendment'].get('sponsor'),
        v['amendment'].get('sponsor_uri'),
        v['amendment'].get('sponsor_party'),
        v['amendment'].get('sponsor_state'),
        v['question'],
        v['question_text'],
        v['description'],
        v['vote_type'],
        v['date'],
        v['time'],
        v['result'],
        v['democratic'].get('yes'),
        v['democratic'].get('no'),
        v['democratic'].get('present'),
        v['democratic'].get('not_voting'),
        v['democratic'].get('majority_position'),
        v['republican'].get('yes'),
        v['republican'].get('no'),
        v['republican'].get('present'),
        v['republican'].get('not_voting'),
        v['republican'].get('majority_position'),
        v['independent'].get('yes'),
        v['independent'].get('no'),
        v['independent'].get('present'),
        v['independent'].get('not_voting'),
        v['total'].get('yes'),
        v['total'].get('no'),
        v['total'].get('present'),
        v['total'].get('not_voting')
    ))
    # read and insert data into house_voting_records
    positions = v.get('positions')
    for p in positions:
        cur.execute('''
            INSERT INTO house_voting_records (
                vote_id,
                member_id,
                vote
            ) VALUES (
                ?, ?, ?
            )
        ''', (
            v['roll_call'], p['member_id'], p['vote_position']
        ))
        # update cycle
        cycle += 1
        # commit
        if cycle % 500 == 0:
            conn.commit()
# final commit
conn.commit()

# read and insert data into senate_votes
cycle = 0
for i in range(1, 2000):
    try:
        fname = senate_prefix + str(i) + suffix
        senate_vote = json.loads(open(fname).read())
        print('Scanning', fname)
    except IOError:
        print('Source exhausted.')
        break
    v = senate_vote['results']['votes']['vote']
    cur.execute('''
        INSERT INTO senate_votes (
            congress,
            session,
            chamber,
            roll_call,
            source,
            url,
            bill_id,
            bill_number,
            bill_api_uri,
            bill_title,
            bill_short_title,
            bill_latest_action,
            amendment_number,
            amendment_api_uri,
            amendment_sponsor_id,
            amendment_sponsor,
            amendment_sponsor_uri,
            amendment_sponsor_party,
            amendment_sponsor_state,
            question,
            question_text,
            description,
            vote_type,
            date,
            time,
            result,
            tie_breaker,
            tie_breaker_vote,
            document_number,
            document_title,
            democratic_yes,
            democratic_no,
            democratic_present,
            democratic_not_voting,
            democratic_majority_position,
            republican_yes,
            republican_no,
            republican_present,
            republican_not_voting,
            republican_majority_position,
            independent_yes,
            independent_no,
            independent_present,
            independent_not_voting,
            total_yes,
            total_no,
            total_present,
            total_not_voting
        ) VALUES (
            ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,
            ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,
            ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,
            ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,
            ?, ?, ?, ?, ?, ?, ?, ?
        )''', (
        v['congress'],
        v['session'],
        v['chamber'],
        v['roll_call'],
        v['source'],
        v['url'],
        v['bill'].get('bill_id'),
        v['bill'].get('number'),
        v['bill'].get('api_uri'),
        v['bill'].get('title'),
        v['bill'].get('short_title'),
        v['bill'].get('latest_action'),
        v['amendment'].get('number'),
        v['amendment'].get('api_uri'),
        v['amendment'].get('sponsor_id'),
        v['amendment'].get('sponsor'),
        v['amendment'].get('sponsor_uri'),
        v['amendment'].get('sponsor_party'),
        v['amendment'].get('sponsor_state'),
        v['question'],
        v['question_text'],
        v['description'],
        v['vote_type'],
        v['date'],
        v['time'],
        v['result'],
        v['tie_breaker'],
        v['tie_breaker_vote'],
        v['document_number'],
        v['document_title'],
        v['democratic'].get('yes'),
        v['democratic'].get('no'),
        v['democratic'].get('present'),
        v['democratic'].get('not_voting'),
        v['democratic'].get('majority_position'),
        v['republican'].get('yes'),
        v['republican'].get('no'),
        v['republican'].get('present'),
        v['republican'].get('not_voting'),
        v['republican'].get('majority_position'),
        v['independent'].get('yes'),
        v['independent'].get('no'),
        v['independent'].get('present'),
        v['independent'].get('not_voting'),
        v['total'].get('yes'),
        v['total'].get('no'),
        v['total'].get('present'),
        v['total'].get('not_voting')
    ))
    # read and insert data into senate_voting_records
    positions = v.get('positions')
    for p in positions:
        cur.execute('''
            INSERT INTO senate_voting_records (
                vote_id,
                member_id,
                vote
            ) VALUES (
                ?, ?, ?
            )
        ''', (
            v['roll_call'], p['member_id'], p['vote_position']
        ))
        # update cycle
        cycle += 1
        # commit
        if cycle % 500 == 0:
            conn.commit()
# final commit
conn.commit()
