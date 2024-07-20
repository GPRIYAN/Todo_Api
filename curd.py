from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class SubPage(BaseModel):
    heading: str | None = "subpage heading"
    description: str | None = "description of subpage"
    footer: str | None = "Footer of subpage"
    page_no: int = 0
    page_dim: float = 0.0


new_dict = {
    100: "sample json",
    0:  {"heading": "subpage heading 0",
         "description": "description of subpage 0",
         "footer": "Footer of subpage 0",
         "page_no": 0,
         "page_dim": 7.67
         }
}

@app.get("/")
async def demo():
    return "First Project"

@app.post('/sub')
async def subPage(sub: SubPage):
    if new_dict.get(sub.page_no):
        new_dict[sub.page_no] = sub
        return "subpage updated"
    else:
        new_dict[sub.page_no] = sub
        return "subpage created"


@app.put("/sub/{page_no}")
async def put_func(page_no: int, sub: SubPage):
    print(new_dict.get(page_no))
    if new_dict.get(page_no):
        new_dict[page_no] = sub
        return "subpage updated"
    else:
        return "subpage cant updated"


@app.delete("/sub/{page_no}")
async def del_fun(page_no: int):
    if new_dict.get(page_no):
        del new_dict[page_no]
        return "subpage deleted"
    else:
        return "subpage not deleted"


@app.patch("/sub/{page_no}")
async def patch_fun(page_no: int, sub: SubPage):
    if new_dict.get(page_no):
        sub_copy = dict(sub)
        for key, value in sub_copy.items():
            new_dict[page_no][key] = sub_copy[key]
        return new_dict
    else:
        return "cant update"