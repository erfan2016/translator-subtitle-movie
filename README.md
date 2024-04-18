## Translate Subtitle Movies

### prerequisite

```python
pip install -r requirment.txt
```

**Example**

```python
# Step 01
test = TranslateSrt("PathFileSubtitle.srt")
# variable test is an object of class TranslateSrt
#Step 02
if test.translate_srt():
    print("OK, success create file translate...")
else:
    print("Opps! Can not create file translate...")
# method test.translate_srt() return result True or False
# if equals to True, so is created a new file of srt with new language, but if equals to False, nothing :)
# Default language to create new file of srt is Persian
# Default language srt file is English
# translate_srt(self, src_language = 'en', dest_language='fa')
```
ERFAN MAHIGIR
