from typing import List, Tuple, Pattern
import json
import re


class PhoneNumbersFilter:
    def __init__(self, phone_type: int, mobile_operator: int, category: List[int], include_numbers: List[int],
                 exclude_numbers: List[int], point_values: str, phone_number_mask: str, phone_number_mask_strict: bool):
        self.__phone_type: int = phone_type
        self.__mobile_operator: int = mobile_operator
        self.__category: List[int] = category
        self.__include_numbers: List[int] = include_numbers
        self.__exclude_numbers:  List[int] = exclude_numbers
        self.__point_values: str = point_values
        self.__phone_number_mask: str = phone_number_mask
        self.__phone_number_mask_strict: bool = phone_number_mask_strict

    def __get_point_values_pattern(self) -> List[Tuple[str, int]]:
        pattern: Pattern[str] = re.compile(r'^\d$')
        target_point_values: List[Tuple[str, int]] = []
        i: int = 0
        for char in self.__point_values:
            if re.match(pattern, char):
                target_point_values.append((str(char), i))
            i += 1
        return target_point_values

    def __get_target_mask_pattern(self) -> List[List[int]]:
        pattern: Pattern[str] = re.compile(r'^[a-z]$')
        target_mask = []
        for char in self.__phone_number_mask:
            if re.match(pattern, str(char).lower()):
                target_mask.append(str(char).lower())
            else:
                target_mask.append(None)

        chars: set = set(target_mask)
        req_matches: List[List[int]] = []
        for item in chars:
            if item is not None:
                req_matches.append([n for n, j in enumerate(target_mask) if j == item])
        return req_matches

    def __validate_number_by_point_values(self, number) -> bool:
        pattern = self.__get_point_values_pattern()
        if pattern.__len__() == 0:
            return True
        for char in pattern:
            if str(number)[char[1]] != char[0]:
                return False
        return True

    def __validate_number_by_target_mask(self, number) -> bool:
        number = str(number)[3:]
        if self.__phone_number_mask.__len__() == 0:
            return True
        target_chars_list = []
        target_mask_pattern = self.__get_target_mask_pattern()
        for char in target_mask_pattern:
            position_check_list = []
            different_chars_list = []
            i = 0
            for item in number:
                if i in char:
                    position_check_list.append(item)
                else:
                    different_chars_list.append(item)
                i += 1

            if position_check_list.__len__() == 0:
                continue
            if set(position_check_list).__len__() > 1:
                return False
            # Strict mask matching
            if self.__phone_number_mask_strict and str(position_check_list[0]) in different_chars_list:
                return False
            target_chars_list.append(position_check_list[0])
        if set(target_chars_list).__len__() < target_mask_pattern.__len__():
            return False
        return True

    def __validate_include_numbers(self, number) -> bool:
        if self.__include_numbers.__len__() == 0:
            return True
        else:
            for i in self.__include_numbers:
                if str(i) in list(number)[3:]:
                    return True
        return False

    def __validate_exclude_numbers(self, number) -> bool:
        if self.__exclude_numbers.__len__() == 0:
            return True
        else:
            for i in self.__exclude_numbers:
                if str(i) in list(number)[3:]:
                    return False
        return True

    def __filter_by_primal_properties(self, raw_phone_numbers_list) -> List[any]:
        filtered_list = []

        for number in raw_phone_numbers_list:
            validity = False
            if int(number['fed_city']) != self.__phone_type:
                continue
            if self.__phone_type == 1:
                num = number['number']

            else:
                num = number['city_number']

            # Category validity check
            if self.__category.__len__() == 0:
                pass
            else:
                if int(float(number['price'])) in self.__category:
                    pass
                else:
                    continue

            if self.__validate_include_numbers(num) and self.__validate_exclude_numbers(num) and \
                    self.__validate_number_by_point_values(num) and self.__validate_number_by_target_mask(num):
                validity = True

            if validity:
                filtered_list.append({
                    'abc_ctn': number['city_number'],
                    'def_ctn': number['number'],
                    'type': number['fed_city'],
                    'price': int(float(number['price']))
                })
        return filtered_list

    def get_filtered_phone_numbers_list(self, raw_phone_numbers_list: List[any]):
        return self.__filter_by_primal_properties(raw_phone_numbers_list)
