# BlenderBIM Add-on - OpenBIM Blender Add-on
# Copyright (C) 2020, 2021 Dion Moult <dion@thinkmoult.com>
#
# This file is part of BlenderBIM Add-on.
#
# BlenderBIM Add-on is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# BlenderBIM Add-on is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with BlenderBIM Add-on.  If not, see <http://www.gnu.org/licenses/>.

import bpy
import ifc5d.qto
from blenderbim.bim.prop import StrProperty, Attribute
from bpy.types import PropertyGroup
from bpy.props import (
    PointerProperty,
    StringProperty,
    EnumProperty,
    BoolProperty,
    IntProperty,
    FloatProperty,
    FloatVectorProperty,
    CollectionProperty,
)


def get_qto_rule(self, context):
    results = []
    for rule_id, rule in ifc5d.qto.rules.items():
        results.append((rule_id, rule["name"], rule["description"]))
    return results


def get_calculator(self, context):
    results = []
    for name, calculator in ifc5d.qto.calculators.items():
        results.append((name, name, calculator.__doc__))
    return results


def get_calculator_function(self, context):
    calculator = ifc5d.qto.calculators[self.calculator]
    results = []
    for function in calculator.get_functions():
        results.append((function.id, function.name, function.description))
    return results


class BIMQtoProperties(PropertyGroup):
    qto_rule: EnumProperty(items=get_qto_rule, name="Qto Rule")
    calculator: EnumProperty(items=get_calculator, name="Calculator")
    calculator_function: EnumProperty(items=get_calculator_function, name="Calculator Function")
    qto_result: StringProperty(default="", name="Qto Result")
    qto_name: StringProperty(name="Qto Name", default="My_Qto")
    prop_name: StringProperty(name="Prop Name", default="MyDimension")
