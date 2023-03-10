from app import db
from app.models.question import Question 


# list of dictionaries, each dict is a question
questions_data = [
    {
        'prompt': 'World War II began what year?',
        'choices': {
            '1': '1917',
            '2': '1932',
            '3': '1945',
            '4': '1939'
        },
        'correct_answer': '4'
    },
    {
        'prompt': 'World War II began when Germany invaded what country?',
        'choices': {
            '1': 'Austria',
            '2': 'Poland',
            '3': 'Belgium',
            '4': 'France'
        },
        'correct_answer': '2'
    },
    {
        'prompt': 'How many years did the war last?',
        'choices': {
            '1': '10',
            '2': '8',
            '3': '13',
            '4': '6'
        },
        'correct_answer': '4'
    },
    {
        'prompt': 'What were the years of the war?',
        'choices': {
            '1': '1939 - 1945',
            '2': '1942 - 1948',
            '3': '1940 - 1951',
            '4': '1932 - 1938'
        },
        'correct_answer': '1'
        },
    {
        'prompt': 'How many people were killed during the war?',
        'choices': {
            '1': '20 million',
            '2': '3 million',
            '3': '70 million',
            '4': '10 million'
        },
        'correct_answer': '3'
    },
    {
        'prompt': 'Which war was deadlier than WWII?',
        'choices': {
            '1': 'World War 1',
            '2': 'The Vietnam War',
            '3': 'The Cold War',
            '4': 'None, WWII was the deadliest war in history'
        },
        'correct_answer': '4'   
    },
    {
        'prompt': 'The Axis powers consisted of what 3 countries?',
        'choices': {
            '1': 'United States, Great Britain, France',
            '2': 'Germany, Italy, and Japan',
            '3': 'USSR, Italy, Germany',
            '4': 'Austria, Germany, USSR'
        },
        'correct_answer': '2'
    },
    {
        'prompt': 'The Allied powers consisted of what 4 countries?',
        'choices': {
            '1': 'United States, Great Britain, France, Canada',
            '2': 'Great Britain, Canada, Australia, United States',
            '3': 'United States, Great Britain, the Soviet Union, and France.',
            '4': 'France, Great Britain, The Netherlands, Poland'
        },
        'correct_answer': '3'
    },
    {
        'prompt': 'The Holocaust was the genocide of how many Jews by the Nazis?',
        'choices': {
            '1': 'six million',
            '2': 'fifteen million',
            '3': 'three million',
            '4': 'one million'
        },
        'correct_answer': '1'
    },
    {
        'prompt': 'What year did the United States enter the war?',
        'choices': {
            '1': '1939',
            '2': '1941',
            '3': '1943',
            '4': '1945'
        },
        'correct_answer': '2'
    },
    {
        'prompt': 'Why did the United States finally enter the war?',
        'choices': {
            '1': 'Germany invaded France',
            '2': 'Germany sunk the Lusitania',
            '3': 'Japan attacked Pearl Harbor',
            '4': 'Allegiance to Great Britain and France'
        },
        'correct_answer': '3'
    },
    {
        'prompt': 'What was D-Day?',
        'choices': {
            '1': 'When Japan attacked Pearl Harbor on December 7, 1941',
            '2': 'The first atomic bomb which was dropped on Hiroshima on August 6, 1945',
            '3': 'The largest amphibious invasion in history, which took place on June 6, 1944',
            '4': 'Germany unconditionally surrendered to the Allies on May 7, 1945 '
        },
        'correct_answer': '3'
    },
    {
        'prompt': 'What was the codename for the Allied Invasion of Normandy in 1944?',
        'choices': {
            '1': 'Operation Stonewall',
            '2': 'Operation Battleaxe',
            '3': 'Operation Scorpion',
            '4': 'Operation Overlord'
        },
        'correct_answer': '4'
    },
    {
        'prompt': 'America\'s top secret Manhattan Project began in what year?',
        'choices': {
            '1': '1942',
            '2': '1944',
            '3': '1943',
            '4': '1941'
        },
        'correct_answer': '1'
    },
    {
        'prompt': 'In which country were the majority of the Nazi extermination camps?',
        'choices': {
            '1': 'Germany',
            '2': 'Poland',
            '3': 'Hungary',
            '4': 'Austria'
        },
        'correct_answer': '2'
    },
    {
        'prompt': 'In what year did Winston Churchill make his "Never was so much owed by so many to so few" speech?',
        'choices': {
            '1': '1939',
            '2': '1942',
            '3': '1940',
            '4': '1938'
        },
        'correct_answer': '3'
    },
    {
        'prompt': 'How did the U.S officially enter the war and specifically with Germany?',
        'choices': {
            '1': 'War was never declared',
            '2': 'Germany declared war',
            '3': 'U.S declared war',
            '4': 'Germany attacked the U.S'
        },
        'correct_answer': '2'
    },
    {
        'prompt': 'Benito Mussolini was the dictator of what country during the war?',
        'choices': {
            '1': 'Italy',
            '2': 'USSR',
            '3': 'Austria',
            '4': 'Hungary'
        },
        'correct_answer': '1'
    },
    {
        'prompt': 'On April 1945 Benito Mussolini was executed in which city?',
        'choices': {
            '1': 'Rome',
            '2': 'Milan',
            '3': 'Naples',
            '4': 'Venice'
        },
        'correct_answer': '2'
    },
    {
        'prompt': 'What was the main dicussion point at the Tehran Conference?',
        'choices': {
            '1': 'The war in the Pacific',
            '2': 'Post-war division of Germany',
            '3': 'The war in North Africa',
            '4': 'Allied invasion of France'
        },
        'correct_answer': '4'
    },
    {
        'prompt': 'What is the name of the project that build the first nuclear weapon?',
        'choices': {
            '1': 'Project Nuclear',
            '2': 'Manhattan Project',
            '3': 'Project Doomsday',
            '4': 'Dark Project'
        },
        'correct_answer': '3'
    },
    {
        'prompt': 'Which US President authorized the atomic bombing of Japan?',
        'choices': {
            '1': 'FDR',
            '2': 'JFK',
            '3': 'Eisonhower',
            '4': 'Truman'
        },
        'correct_answer': '4'
    },
    {
        'prompt': 'Franklin D. Roosevelt died on April 12, 1945 making who become president?',
        'choices': {
            '1': 'Truman',
            '2': 'Eisonhower',
            '3': 'Hoover',
            '4': 'JFK'
        },
        'correct_answer': '1'
    },
    {
        'prompt': 'Why did the United States finally enter the war?',
        'choices': {
            '1': 'Germany invaded France',
            '2': 'Germany sunk the Lusitania',
            '3': 'Japan attacked Pearl Harbor',
            '4': 'Allegiance to Great Britain and France'
        },
        'correct_answer': '3'
    },
    {
        'prompt': 'Who served as Supreme Commander of the Allied Expeditionary Force in Europe?',
        'choices': {
            '1': 'Winston Churchill',
            '2': 'Dwight D. Eisonhower',
            '3': 'Douglas MacArthur',
            '4': 'Charles de Gaulle'
        },
        'correct_answer': '2'
    },
    {
        'prompt': 'Who was the president of France?',
        'choices': {
            '1': 'Charles de Gaulle',
            '2': 'George S. Patton',
            '3': 'Neville Chamberlain',
            '4': 'Winston Churchill'
        },
        'correct_answer': '1'
    },
    {
        'prompt': 'The D-Day landings took place where?',
        'choices': {
            '1': 'Dunkirk',
            '2': 'Normandy',
            '3': 'Tunisia',
            '4': 'The Phillipines'
        },
        'correct_answer': '2'
    },
    {
        'prompt': 'In what year did Italy invade Greece?',
        'choices': {
            '1': '1938',
            '2': '1939',
            '3': '1940',
            '4': '1942'
        },
        'correct_answer': '3'
    },
    {
        'prompt': 'Greenland was occupied by which country on April 1941?',
        'choices': {
            '1': 'USA',
            '2': 'Britain',
            '3': 'Germany',
            '4': 'Italy'
        },
        'correct_answer': '1'
    },
    {
        'prompt': 'Which country suffered the largest number of civilian deaths?',
        'choices': {
            '1': 'Germany',
            '2': 'Soviet Union',
            '3': 'United States',
            '4': 'Great Britain'
        },
        'correct_answer': '2'
    },
    {
        'prompt': 'Which of these countries was not a combatant during the war?',
        'choices': {
            '1': 'The Netherlands',
            '2': 'Poland',
            '3': 'Denmark',
            '4': 'Portugal'
        },
        'correct_answer': '4'
    },
    {
        'prompt': 'How many European countries remained neutral throughout the war?',
        'choices': {
            '1': '3: Sweden, Switzerland, Norway',
            '2': '1: Switzerland',
            '3': '4: Scotland, Denmark, Sweden, Spain',
            '4': '6: Ireland, Portugal, Spain, Sweden, Switzerland, Turkey '
        },
        'correct_answer': '4'
    },
    {
        'prompt': 'Britain declared war on Nazi Germany in what year?',
        'choices': {
            '1': '1940',
            '2': '1939',
            '3': '1941',
            '4': '1938'
        },
        'correct_answer': '2'
    },
    {
        'prompt': 'In what country was the formal surrender of all German forces accepted by the Allies?',
        'choices': {
            '1': 'Germany',
            '2': 'France',
            '3': 'Austria',
            '4': 'Switzerland'
        },
        'correct_answer': '2'
    },
    {
        'prompt': 'What prompted Britain and France to declare war on Germany?',
        'choices': {
            '1': 'Germany invaded France',
            '2': 'Germany invaded Belgium',
            '3': 'Germany invaded Britain',
            '4': 'Germany invaded Poland'
        },
        'correct_answer': '4'
    },
    {
        'prompt': 'Germany invaded which countries May 10, 1940?',
        'choices': {
            '1': 'The Netherlands, Belgium, Luxembourg, France',
            '2': 'France, Belgium',
            '3': 'Poland, Austria, Hungary',
            '4': 'France'
        },
        'correct_answer': '1'
    },
    {
        'prompt': 'What was the code name given to Germany\'s plan to invade the Soviet Union?',
        'choices': {
            '1': 'Operation Barbarossa',
            '2': 'Operation Midnight',
            '3': 'Operation Desert Storm',
            '4': 'Operation V2'
        },
        'correct_answer': '1'
    },
]



