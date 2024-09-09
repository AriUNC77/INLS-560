#Mad lib example for functions.

def coaster_madlib(noun_1, noun_2, noun_3, adjective_1, adjective_2, adjective_3, adverb_1, adverb_2):
    '''Mad lib function'''

    story=f'''
    The Johnson family was thrilled as they arrived at {noun_1} Park. They had been planning this trip for months and couldn't wait to experience all the exciting rides and attractions. As soon as they walked through the entrance, they were greeted by a {adjective_1} parade featuring colorful floats and cheerful performers. The kids, Emily and Jack, were especially excited to ride the {noun_2} . First on their list was the infamous {adjective_2} roller coaster, which promised to deliver a thrilling experience. They queued up {adverb_1} and couldn’t stop talking about how much fun they were going to have. When it was finally their turn, the ride did not disappoint. The twists and turns made them scream {adverb_2} , but they loved every second of it. After the roller coaster, the family decided to grab a bite to eat at a nearby {noun_3} . They enjoyed some delicious food and chatted about their favorite parts of the day. As the sun began to set, they watched the spectacular fireworks show, which was the perfect ending to their {adjective_3} day at the park. Exhausted but happy, they headed home with memories they would cherish forever.
    '''

    return story

output_story =  coaster_madlib("Bear", "Slime Bucket", 'Bumblebee', 'sticky', "smelly", 'wormy', "quickly", 'slowly')

print(output_story)