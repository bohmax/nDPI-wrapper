#include <ndpiReader.c>

int ndpi_wrap_get_api_version(){
	return NDPI_API_VERSION;
}

int ndpi_wrap_ndpi_num_fds_bits(){
	return NDPI_NUM_FDS_BITS;
}

int ndpi_wrap_num_custom_categories(){
	return NUM_CUSTOM_CATEGORIES;
}

int ndpi_wrap_custom_category_label_len(){
	return CUSTOM_CATEGORY_LABEL_LEN;
}

int ndpi_wrap_ndpi_max_supported_protocols(){
	return NDPI_MAX_SUPPORTED_PROTOCOLS;
}

int ndpi_wrap_ndpi_max_num_custom_protocols(){
	return NDPI_MAX_NUM_CUSTOM_PROTOCOLS;
}

int ndpi_wrap_ndpi_procol_size(){
	return NDPI_PROTOCOL_SIZE;
}

void ndpi_wrap_NDPI_BITMASK_SET_ALL(NDPI_PROTOCOL_BITMASK* bitmask){
	NDPI_ONE(bitmask);
}