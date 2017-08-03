from inspect import signature

def clip(text:str,max_len:'int > 0'=80) -> str:
    """ Return text clipped at the last space before or after max_len"""
    end = None
    if len(text)> max_len:
        space_before = text.rfind(' ', 0, max_len)
        if space_before >= 0:
            end = space_before
        else:
            space_after = text.rfind(' ',max_len)
            if space_after >=0:
                end = space_after
    if end is None:
        end = len(text)
    return text[:end].rstrip()


sig = signature(clip)

print(clip.__annotations__)
print(sig.return_annotation)
for param in sig.parameters.values():
    note = repr(param.annotation).ljust(13)
    print(note,':',param.name,'=',param.default)