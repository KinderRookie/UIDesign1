import openai
import os
import random
from PIL import Image, ImageDraw, ImageFont
from flask import Flask, render_template, request, redirect, url_for, session, jsonify, send_file
app = Flask(__name__)
openai.api_key = "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"

card_memory = []

tarot_data = {
    0: {
        "card_index": 0,
        "card_name": "The Fool",
        "upright_meaning": "Beginnings, Spontaneity, Innocence",
        "reverse_meaning": "Recklessness, Folly, Naivety"
    },
    1: {
        "card_index": 1,
        "card_name": "The Magician",
        "upright_meaning": "Manifestation, Resourcefulness, Power",
        "reverse_meaning": "Manipulation, Misuse of Power, Poor Planning"
    },
    2: {
        "card_index": 2,
        "card_name": "The High Priestess",
        "upright_meaning": "Intuition, Unconscious, Inner Voice",
        "reverse_meaning": "Lack of Center, Lost Inner Voice, Repression"
    },
    3: {
        "card_index": 3,
        "card_name": "The Empress",
        "upright_meaning": "Fertility, Femininity, Beauty",
        "reverse_meaning": "Creative Block, Dependence on Others"
    },
    4: {
        "card_index": 4,
        "card_name": "The Emperor",
        "upright_meaning": "Authority, Structure, Control",
        "reverse_meaning": "Tyranny, Rigidity, Coldness"
    },
    5: {
        "card_index": 5,
        "card_name": "The Hierophant",
        "upright_meaning": "Spiritual Wisdom, Religious Dogma, Tradition",
        "reverse_meaning": "Personal Belief System, Freedom, Challenge"
    },
    6: {
        "card_index": 6,
        "card_name": "The Lovers",
        "upright_meaning": "Love, Harmony, Relationships",
        "reverse_meaning": "Self-Love, Disharmony, Imbalance"
    },
    7: {
        "card_index": 7,
        "card_name": "The Chariot",
        "upright_meaning": "Control, Willpower, Success",
        "reverse_meaning": "Self-Aggrandizement, Lack of Control, Opposition"
    },
    8: {
        "card_index": 8,
        "card_name": "Strength",
        "upright_meaning": "Strength, Courage, Patience",
        "reverse_meaning": "Weakness, Self-Doubt, Lack of Discipline"
    },
    9: {
        "card_index": 9,
        "card_name": "The Hermit",
        "upright_meaning": "Soul-Searching, Introspection, Being Alone",
        "reverse_meaning": "Isolation, Loneliness, Withdrawal"
    },
    10: {
        "card_index": 10,
        "card_name": "Wheel of Fortune",
        "upright_meaning": "Change, Cycles, Inevitable Fate",
        "reverse_meaning": "No Control, Clinging to Control, Bad Luck"
    },
    11: {
        "card_index": 11,
        "card_name": "Justice",
        "upright_meaning": "Justice, Fairness, Truth",
        "reverse_meaning": "Unfairness, Lack of Accountability, Dishonesty"
    },
    12: {
        "card_index": 12,
        "card_name": "The Hanged Man",
        "upright_meaning": "Sacrifice, Release, Martyrdom",
        "reverse_meaning": "Martyrdom, Unnecessary Sacrifice, Fear of Sacrifice"
    },
    13: {
        "card_index": 13,
        "card_name": "Death",
        "upright_meaning": "Endings, Change, Transformation",
        "reverse_meaning": "Resistance to Change, Personal Transformation, Inner Purging"
    },
    14: {
        "card_index": 14,
        "card_name": "Temperance",
        "upright_meaning": "Balance, Moderation, Patience",
        "reverse_meaning": "Imbalance, Excess, Self-Healing"
    },
    15: {
        "card_index": 15,
        "card_name": "The Devil",
        "upright_meaning": "Shadow Self, Attachment, Addiction",
        "reverse_meaning": "Releasing Limiting Beliefs, Exploration, Opening Up"
    },
    16: {
        "card_index": 16,
        "card_name": "The Tower",
        "upright_meaning": "Sudden Change, Upheaval, Chaos",
        "reverse_meaning": "Personal Transformation, Fear of Change, Avoidance"
    },
    17: {
        "card_index": 17,
        "card_name": "The Star",
        "upright_meaning": "Hope, Faith, Rejuvenation",
        "reverse_meaning": "Faithlessness, Discouragement, Insecurity"
    },
    18: {
        "card_index": 18,
        "card_name": "The Moon",
        "upright_meaning": "Illusion, Fear, Subconscious",
        "reverse_meaning": "Release of Fear, Re-Evaluation, Inner Confusion"
    },
    19: {
        "card_index": 19,
        "card_name": "The Sun",
        "upright_meaning": "Positivity, Fun, Warmth, Success",
        "reverse_meaning": "Inner Child, Feeling Down, Depressed"
    },
    20: {
        "card_index": 20,
        "card_name": "Judgement",
        "upright_meaning": "Judgement, Rebirth, Inner Calling",
        "reverse_meaning": "Self-Doubt, Inner Critic, Ignoring the Call"
    },
    21: {
        "card_index": 21,
        "card_name": "The World",
        "upright_meaning": "Completion, Integration, Accomplishment",
        "reverse_meaning": "Seeking Personal Closure, Shortcuts, No Closure"
    },
    
}

@app.route('/')
def index():
    return render_template('proto.html')



@app.route('/tarot', methods=['POST'])
def get_tarot():
    numbers = random.sample(range(0, 22), 3)
    card_memory = numbers
    choice = [tarot_data[numbers[0]]['card_name'], tarot_data[numbers[1]]['card_name'], tarot_data[numbers[2]]['card_name']]
    st = str(choice.pop())+", "+str(choice.pop())+", and "+str(choice.pop())
    q = request.form['question']
    chat = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role":"system", "content":"You are a AI tarot reader. You give advice to people based on their tarot card. And please use the following format: 'I has following question: <question>, and my tarot card is <tarot card>.'"},
                  {"role":"user", "content":"I has following question: "+q+", and my tarot card is "+st+". Every each card, change line add one more line."}],

        temperature=0.6,
        max_tokens=600,
        top_p=1,
    )
    st = [numbers[2], numbers[1], numbers[0]]
    return render_template('answer.html', cards=st, answer=chat.choices[0].message.content)



    

if __name__ == '__main__':

    app.run(debug=True)