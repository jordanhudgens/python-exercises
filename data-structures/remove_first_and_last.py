def remove_first_and_last(list_to_clean):
  _, *content, _ = list_to_clean
  return content


html = ['<h1>', 'My content', '</h1>']

print(remove_first_and_last(html))

other_content_to_clean = ['', 'My content', 'Something else', '/']

print(remove_first_and_last(other_content_to_clean))
