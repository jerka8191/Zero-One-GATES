from obj.gate import Gate

class GateTest:

    def run(self):
        gate = Gate()
        # AND
        assert not gate.AND(False, False)
        assert not gate.AND(False, True)
        assert not gate.AND(True, False)
        assert gate.AND(True, True)
        assert gate.AND(314, "value") is None
        # NAND
        assert gate.NAND(False, False)
        assert gate.NAND(False, True)
        assert gate.NAND(True, False)
        assert gate.NAND(2.718, "default") is None
        assert not gate.NAND(True, True)
        # OR
        assert not gate.OR(False, False)
        assert gate.OR(False, True)
        assert gate.OR(True, False)
        assert gate.OR(True, True)
        assert gate.OR(3.14, "true") is None
        # NOR
        assert gate.NOR(False, False)
        assert not gate.NOR(False, True)
        assert not gate.NOR(True, False)
        assert not gate.NOR(True, True)
        assert gate.NOR(2718, "false") is None
        # XOR
        assert not gate.XOR(False, False)
        assert gate.XOR(False, True)
        assert gate.XOR(True, False)
        assert not gate.XOR(True, True)
        assert gate.XOR(27, "test") is None
        # XNOR
        assert gate.XNOR(False, False)
        assert not gate.XNOR(False, True)
        assert not gate.XNOR(True, False)
        assert gate.XNOR(True, True)
        assert gate.XNOR(18, "placeholder_text_value") is None
        # NOT
        assert gate.NOT(False)
        assert not gate.NOT(True)
        assert gate.NOT("not") is None
