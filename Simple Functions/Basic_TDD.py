# this won't work alone, but the principle is using the test code to test the for loop. This one comes from a codewars example.

websites = ['codewars' for _ in range(1000)]

test.assert_equals(len(websites), 1000)
test.assert_equals(type(websites), list)
test.assert_equals(list(set(websites)), ["codewars"])

