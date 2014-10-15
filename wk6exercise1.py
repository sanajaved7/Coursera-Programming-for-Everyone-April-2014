text = "X-DSPAM-Confidence:    0.8475"
col = text.find(':')
print col
end = len(text)
print end
num = text[col+1:end]
print float(num)