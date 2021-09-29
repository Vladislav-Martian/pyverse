from pyvorse.data.positioned import poslist
from unittest.runner import TextTestResult
from pyvorse import __version__
from unittest import TestCase, main
from pyvorse.core import *
from pyvorse.data import *
from pyvorse.mathematics import *
from pyvorse.tests import *
from pyvorse.pipeline import *


class TestCore(TestCase):
    def test_attribute_decor(self):
        "Attribute decorator, that turns function to object, that processes attribute names with this function."
        @attribute
        def case(name:str):
            return name + "_ending"
        
        self.assertEqual(case.testword, "testword_ending")
    
    def test_throws_decor(self):
        "Decorator adds for function attribute __throws__, that saves list of error classes."

        @throws(ValueError)
        def case():
            raise ValueError("TestError")
        
        self.assertTrue(isthrows(case, ValueError), True)

    def test_try_call(self):
        "Function, that allows to shortly call safe variation of function by trycall."
        @throws(ValueError)
        def case():
            raise ValueError("TestError")
        
        try:
            result, error = trycall(case)
            self.assertIsInstance(error, ValueError, "Wrong error type")
            self.assertEqual(result, None, "Wrong result value")
        except Exception as e:
            self.fail("trycall doesnt work")

    def test_safe_call(self):
        "Decorator, turns function to safe variant, returns same tuple, as trycall(function)."
        @safe
        def case():
            raise ValueError("TestError")
        
        try:
            result, error = case()
            self.assertIsInstance(error, ValueError, "Wrong error type")
            self.assertEqual(result, None, "Wrong result value")
        except Exception as e:
            self.fail(f"{e}")
    
    def test_callonoperator_decor(self):
        "Simplistic attribute, allows you to conver any function to operand."
        @calloperators(Operators.All)
        def case(value):
            return value
        
        self.assertTrue(case - True)

    def test_functor(self):
        "Edits function, to call it with this function instace as first argument."

        @functor
        def case(func, value):
            func.val = value
        
        case(True) # assigns .val to function. case.val must be True

        self.assertTrue(case.val)
    

    def test_copy_all_props(self):
        x = basis()
        x.f = 0
        x.ff = 1
        x.fff = 2
        x.__fff = 2
        y = basis()

        copyAllProps(y, x)
        self.assertTrue(y.f == 0)
        self.assertTrue(y.ff == 1)
        self.assertTrue(y.fff == 2)
        self.assertTrue(not hasattr(y, "__fff"))


class TestDataDeep(TestCase):
    def test_deep_access(self):
        # create deep object class
        cl1 = dci.extend(deep({
            "alpha": 0,
            "beta": 1,
            "gamma": 2,
            "delta": 3
        }))

        # deep object instance
        ins1 = cl1.new()

        # extend deep class
        cl2 = cl1.extend(deep({
            "unknown": None
        }))
        # extended instance
        ins2 = cl2.new()

        self.assertTrue(ins2.unknown == None)
        self.assertTrue(ins2.delta == 3)


class TestDataPos(TestCase):
    def test_poslist(self):
        x = poslist()

        x.appends(None, 1, 2, None)

        self.assertEqual(repr(x), "{1: 1, 2: 2}")
        self.assertEqual(x[1], 1)
        self.assertEqual(x[2], 2)


class TestDataSimple(TestCase):
    def test_loop(self):
        l = loop([0, 1, 2])
        self.assertTrue(l[3] == 0)
    
    def test_scope(self):
        s = scope({
                "alpha": 1,
                "beta": 2
            })
        
        self.assertTrue(s.alpha == 1)
        self.assertTrue(s(1) == 2)
        s.alpha = 2
        self.assertTrue(s.alpha == 2)
        self.assertTrue(s.alpha == s["alpha"])

        s["dynamic"] = lambda x: x.alpha + x.beta

        self.assertTrue(s.getDynamic("dynamic") == 4)

    def test_stack(self):
        s = stack()
        s.push(0)
        s.pushes(1, 2, 3, 4, 5, 6, 7, 8, 9)

        i = 10
        while not s.empty():
            i -= 1
            #============
            pull = s.pull()
            self.assertTrue(i == pull, f"Value: {pull} / Must: {i} / {s}")

        self.assertTrue(s.empty())
    
    def test_validation(self):
        s = stack().setvalidation(lambda s, val: isinstance(val, int))
        with self.assertRaises(ValueError):
            s.leftpushes(0, 1, 2, None, 3, 4, 5, 6, 7, 8, 9)
        
finder = lambda val, *d: val % 2 == 0
class TestDataSmart(TestCase):
    example = smartlist([0,1,2,3,4,5,6,7,8,9])
    c = 0

    def test_smartlist_find(self):
        item, index = self.example.find(lambda val, i, l: val == 6)
        self.assertEqual(item, 6, f"item = {item}")
        self.assertEqual(index, 6, f"index = {item}")

    def test_smartlist_select(self):
        item = self.example.select(lambda val, i, l: val == 6)
        self.assertEqual(item, 6, f"item = {item}")
    
    def test_smartlist_filtered(self):
        x = 0
        for a in self.example.filtered(finder):
            x += 1
        self.assertEqual(x, 5)
    
    def test_smartlist_filter(self):
        x = self.example.filter(finder)
        self.assertEqual(len(x), 5)
        self.assertIsInstance(x, smartlist)

    def test_smartlist_any(self):
        x = self.example.any(finder)
        self.assertTrue(x)
    
    def test_smartlist_all(self):
        x = self.example.all(finder)
        self.assertFalse(x)
    
    def test_smartlist_mapper(self):
        x = self.example.mapper(finder)
        y = True
        for a in x:
            self.assertTrue(a == y)
            y = not y
    
    def test_smartlist_reducer(self):
        x = self.example.reducer(lambda prev, now, *z: prev + now, 0)
        self.assertEqual(x, 45)

    def test_smartlist_sort(self):
        self.example.reverse()
        x = self.example.sort(lambda x, y: 1 if x < y else 0 if x == y else -1)
        self.assertEqual(repr(x), "[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]")


class TestDataSmart2(TestCase):
    example = [{
        "a": {
            "b": [1, 2, 3, 4]
        }
    }]

    def test_handle(self):
        def h(box):
            box.inbox += 1
        
        x = handle()(h)(h)

        y = x.use(0)
        self.assertEqual(y.inbox, 2)
    
    def test_objectAddress(self):
        x = objectAddress()[0]["a"]["b"][-1]

        self.assertEqual(x.use(self.example), 4)


class TestDataSpiders(TestCase):
    example = [[[[[[0]]]]]]

    def test_spider(self):
        x = 0

        def seeker(struct, dot, box):
            if not isinstance(dot[0], int):
                return dot[0]
            else:
                box.stop()

        def worker(struct, dot, box):
            nonlocal x
            x += 1
        
        spider(seeker, worker).use(self.example)

        self.assertEqual(x, 6)


class TestDataTable(TestCase):
    def test_tables(self):
        t = Table()
        t.adddefaultheader(w.index, -1, lambda tbl, row, col: row) # dynamic value for getdynamic
        t.adddefaultheader(w.name, 1, "Unknown")
        t.adddefaultheader(w.lastname, -1, "Unknown")
        t.adddefaultheader(w.age, 0 , "unknown")

        t.appends()
        t.appends(None, "XTL")
        t.appends(None, "XTL", "U90")
        t.appends(None, "XTL", "U90", 40)
        t.appends(None, "XTL", None, 90)

        
        self.assertEqual(t[2][2], "U90")
        self.assertEqual(t.getdynamic(2, 0), 2)
        self.assertEqual(t.getdynamic(4, 2), "Unknown")


class TestMathematics(TestCase):
    def test_mathematics(self):
        self.assertEqual(7, hexcount(2))
        self.assertEqual(10, trin(4))


class TestTests(TestCase):
    def test_all_exprs(self):
        self.assertTrue(instanceof(0, int, float))
        self.assertTrue(iterable([0]))
        self.assertTrue(forable([0]))
        self.assertFalse(isinrange([0], 1))
    
    def test_all_other(self):
        x = basis()
        y = basis()
        z = {
            0: 0
        }
        self.assertTrue(isand(x, x, x))
        self.assertTrue(isor(x, y, x))
        self.assertTrue(eqand(0, 0, 1 - 1))
        self.assertTrue(eqor(0, 1, 1 - 1))
        self.assertTrue(hashable("w"))
        self.assertTrue(haskey(z, 0))
        self.assertTrue(haslen([]))


class TestPipeline(TestCase):
    def test_piplines(self):
        # build router
        pip = DictionaryPipeline()

        @pip
        def first(box, meta):
            box[0] += 1
            box['target'] = "second"
        
        @pip
        def second(box, meta):
            box[0] += 2
            box['target'] = "third"
        
        @pip
        def third(box, meta):
            box[0] += 3
            box.stop()
        
        route = router(pip.defaultpointer)

        @route.initalizer
        def inits(box, meta):
            box[0] = 0
            box['target'] = "first"
        
        @route.finalizer
        def finile(box, meta):
            box.inbox = box[0]
        
        cell = dcell()
        # using router
        route(cell)
        self.assertTrue(cell.inbox == 6, "router doesn`t works")





if __name__ == '__main__':
    main()
