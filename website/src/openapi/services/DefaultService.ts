/* generated using openapi-typescript-codegen -- do not edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { WithinSimilarResponse } from '../models/WithinSimilarResponse';
import type { CancelablePromise } from '../core/CancelablePromise';
import { OpenAPI } from '../core/OpenAPI';
import { request as __request } from '../core/request';
export class DefaultService {
    /**
     * Get
     * @returns any Successful Response
     * @throws ApiError
     */
    public static get(): CancelablePromise<any> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/test',
        });
    }
    /**
     * Within Similar
     * @returns WithinSimilarResponse Successful Response
     * @throws ApiError
     */
    public static withinSimilar(): CancelablePromise<WithinSimilarResponse> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/within-similar',
        });
    }
}
