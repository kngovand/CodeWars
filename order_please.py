def order(sentence):
    # code here
    counter = 1
    sentence = sentence.split(" ")
    ordered = []

    for x in range(len(sentence)):
        for i in sentence:
            if str(counter) in i:
                ordered.append(i)
                counter += 1

    final_sentence = ' '.join(ordered)

    return final_sentence