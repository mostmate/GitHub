from profanity_check import predict, predict_prob

#predict(['takes array and returns 1 for each string if offensive, else 0.'])
# [0]
x = predict(['bad'])
print(x)
#predict(['fuck you'])
# [1]

#predict_prob(['takes array and returns probability if each string is offensive'])
# [0.08686173]

#predict_prob(['go to hell, you scum'])
# [0.7618861]
