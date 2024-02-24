from aiogram.fsm.state import State,StatesGroup

class CategoryState(StatesGroup):
    addcategory = State()

    startEditCategoryState = State()
    finishEditCategoryState = State()

    startDeleteCategoryState = State()
    finishDeleteCategoryState = State()

    addproduct = State()

    startEditProductState = State()
    finishEditProductState = State()

    startDeleteProductState = State()
    finishDeleteProductState = State()