from .custom_reduce_cuda import all_reduce as _all_reduce
from .custom_reduce_cuda import dispose as _dispose
from .custom_reduce_cuda import init_custom_ar as _init_custom_ar
from .moe_align_block_size import moe_align_block_size as _moe_align_block_size
from .warp_reduce_cuda import reduce as _reduce


def warp_reduce(input_tensor):
    return _reduce(input_tensor)


def init_custom_reduce(rank_id, num_devices, buffers, barrier_in, barrier_out):
    return _init_custom_ar(rank_id, num_devices, buffers, barrier_in, barrier_out)


def custom_dispose(fa):
    _dispose(fa)


def custom_reduce(fa, inp, out):
    _all_reduce(fa, inp, out)


def moe_align_block_size(
    topk_ids,
    num_experts,
    block_size,
    sorted_token_ids,
    experts_ids,
    num_tokens_post_pad,
):
    _moe_align_block_size(
        topk_ids,
        num_experts,
        block_size,
        sorted_token_ids,
        experts_ids,
        num_tokens_post_pad,
    )
