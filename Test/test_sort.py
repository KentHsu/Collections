import pytest
from ..sort_collection import Insertion
from ..sort_collection import Selection
from ..sort_collection import Exchange
from ..sort_collection import Merge
from ..sort_collection import Distribution
from ..sort_collection import Tim


@pytest.fixture
def nums():
	import random
	nums = list(range(100))
	random.shuffle(nums)
	return nums


def test_insertion_sort(nums):
	sorting = Insertion.direct_insertion_sort
	assert sorting(nums) == sorted(nums)

def test_binary_insertion_sort(nums):
	sorting = Insertion.binary_insertion_sort
	assert sorting(nums) == sorted(nums)

def test_shell_sort(nums):
	sorting = Insertion.shell_sort
	assert sorting(nums) == sorted(nums)

def test_seleciton_sort(nums):
	sorting = Selection.direct_selection_sort
	assert sorting(nums) == sorted(nums)

def test_heap_sort(nums):
	sorting = Selection.heap_sort
	assert sorting(nums) == sorted(nums)

def test_bubble_sort(nums):
	sorting = Exchange.bubble_sort
	assert sorting(nums) == sorted(nums)

def test_cocktaill_sort(nums):
	sorting = Exchange.cocktail_sort
	assert sorting(nums) == sorted(nums)

def test_quick_sort(nums):
	sorting = Exchange.quick_sort
	assert sorting(nums) == sorted(nums)

def test_merge_sort_top_down(nums):
	sorting = Merge.top_down
	assert sorting(nums) == sorted(nums)

def test_merge_sort_bottom_up(nums):
	sorting = Merge.bottom_up
	assert sorting(nums) == sorted(nums)

def test_counting_sort(nums):
	sorting = Distribution.counting_sort
	assert sorting(nums) == sorted(nums)

def test_bucket_sort(nums):
	sorting = Distribution.bucket_sort
	assert sorting(nums) == sorted(nums)

def test_radix_sort(nums):
	sorting = Distribution.radix_sort
	assert sorting(nums) == sorted(nums)

def test_tim_sort(nums):
	sorting = Tim.tim_sort
	assert sorting(nums) == sorted(nums)

